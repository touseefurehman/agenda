from django.contrib import admin
from django.forms import TimeInput
from django.db import models
from .models import EventDay, Event, Speaker


# ----------------------------
# Inline for Speakers in Event
# ----------------------------
class SpeakerInline(admin.TabularInline):
    model = Speaker
    extra = 1  # Show 1 blank form by default
    fields = ('name', 'designation', 'organization', 'photo')
    readonly_fields = ()  # All editable, optional
    can_delete = True  # Allow removing speakers
    verbose_name = "Speaker"
    verbose_name_plural = "Speakers"


# ----------------------------
# Event Admin
# ----------------------------
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'start_time', 'end_time', 'duration', 'forum')
    readonly_fields = ('duration',)  # Duration is auto-calculated
    inlines = [SpeakerInline]  # Add multiple speakers inline
    list_filter = ('day',)  # Filter events by day
    search_fields = ('title', 'forum', 'speakers__name')  # Search by event and speaker

    formfield_overrides = {
        models.TimeField: {
            'widget': TimeInput(attrs={'type': 'time', 'step': 60})  # Time picker
        }
    }


# ----------------------------
# EventDay Admin
# ----------------------------
@admin.register(EventDay)
class EventDayAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    inlines = []  # Optional: you could add EventInline if desired


# ----------------------------
# Optional: Speaker Admin (for direct editing)
# ----------------------------
@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'designation', 'organization')
    list_filter = ('event',)
    search_fields = ('name', 'organization', 'designation')
