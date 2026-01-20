from django.contrib import admin
from django.forms import TimeInput
from django.db import models
from django.utils.html import mark_safe
from django import forms

from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import CSV
from import_export import resources, fields
from import_export.widgets import CharWidget

from .models import EventDay, Event, Speaker


# =================================================
# Speaker Resource (Import / Export)
# =================================================
class SpeakerResource(resources.ModelResource):
    photo_url = fields.Field(
        column_name='photo_url',
        attribute='photo',
        widget=CharWidget()
    )

    class Meta:
        model = Speaker
        fields = ('name', 'designation', 'organization', 'photo_url')
        export_order = ('name', 'designation', 'organization', 'photo_url')
        import_id_fields = ()


# =================================================
# Speaker Admin
# =================================================
@admin.register(Speaker)
class SpeakerAdmin(ImportExportModelAdmin):
    resource_class = SpeakerResource
    list_display = ('photo_preview', 'name', 'designation', 'organization')
    search_fields = ('name', 'designation', 'organization')
    list_filter = ('organization',)
    formats = [CSV]

    def photo_preview(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" style="height:42px;border-radius:6px;" />'
            )
        return "—"

    photo_preview.short_description = "Photo"


# =================================================
# Event Admin Form (Hide Already Selected Speakers)
# =================================================
class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Exclude already-selected speakers from the selectable list
            self.fields['speakers'].queryset = Speaker.objects.exclude(
                pk__in=self.instance.speakers.values_list('pk', flat=True)
            )
        else:
            self.fields['speakers'].queryset = Speaker.objects.all()


# =================================================
# Event Admin
# =================================================
@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    form = EventAdminForm

    list_display = (
        'title',
        'day',
        'start_time',
        'end_time',
        'duration',
        'forum',
    )
    list_filter = ('day',)
    search_fields = ('title', 'forum')
    readonly_fields = ('duration',)
    raw_id_fields = ('speakers',)  # clean UI for selecting existing speakers
    formats = [CSV]

    formfield_overrides = {
        models.TimeField: {'widget': TimeInput(attrs={'type': 'time'})}
    }

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'day', 'forum')
        }),
        ('Schedule', {
            'fields': ('start_time', 'end_time', 'duration')
        }),
        ('Speakers', {
            'fields': ('speakers',),
            'description': 'Select speakers not already added to this event.',
        }),
    )


# =================================================
# Event Inline (inside EventDay)
# =================================================
class EventInline(admin.StackedInline):
    model = Event
    extra = 1
    readonly_fields = ('duration',)
    raw_id_fields = ('speakers',)

    formfield_overrides = {
        models.TimeField: {'widget': TimeInput(attrs={'type': 'time'})}
    }


# =================================================
# EventDay Admin
# =================================================
@admin.register(EventDay)
class EventDayAdmin(ImportExportModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    inlines = [EventInline]
    formats = [CSV]
