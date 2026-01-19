from django.contrib import admin
from django.forms import TimeInput
from django.db import models
from .models import EventDay, Event, Speaker

# ----------------------------
# Event Admin
# ----------------------------
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'start_time', 'end_time', 'duration', 'forum')
    readonly_fields = ('duration',)
    list_filter = ('day', 'speakers')
    search_fields = ('title', 'forum', 'speakers__name')
    filter_horizontal = ('speakers',)  # <-- nice multi-select widget for ManyToMany
    formfield_overrides = {
        models.TimeField: {'widget': TimeInput(attrs={'type': 'time', 'step': 60})}
    }

# ----------------------------
# EventDay Admin with inline Events
# ----------------------------
class EventInline(admin.TabularInline):
    model = Event
    extra = 1
    fields = ('title', 'start_time', 'end_time', 'duration', 'forum', 'speakers')
    readonly_fields = ('duration',)
    filter_horizontal = ('speakers',)
    formfield_overrides = {
        models.TimeField: {'widget': TimeInput(attrs={'type': 'time', 'step': 60})}
    }

@admin.register(EventDay)
class EventDayAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    inlines = [EventInline]  # <-- Events are grouped under EventDay

# ----------------------------
# Speaker Admin
# ----------------------------
@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'organization')
    search_fields = ('name', 'organization', 'designation')
