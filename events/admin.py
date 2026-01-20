from django.contrib import admin
from django.forms import TimeInput
from django.db import models
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import CSV
from import_export import resources, fields
from import_export.widgets import CharWidget
from .models import EventDay, Event, Speaker


# ----------------------------
# Speaker Resource for Import/Export
# ----------------------------
class SpeakerResource(resources.ModelResource):
    photo_url = fields.Field(
        column_name='photo_url',  # exported CSV column name
        attribute='photo',        # CloudinaryField in your model
        widget=CharWidget()
    )

    class Meta:
        model = Speaker
        # Only export/import these fields
        fields = ('name', 'designation', 'organization', 'photo_url')
        export_order = ('name', 'designation', 'organization', 'photo_url')
        import_id_fields = ()  # Do not require 'id' in CSV to import


# ----------------------------
# Event Admin with Import/Export
# ----------------------------
@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    list_display = ('title', 'day', 'start_time', 'end_time', 'duration', 'forum')
    readonly_fields = ('duration',)
    list_filter = ('day', 'speakers')
    search_fields = ('title', 'forum', 'speakers__name')
    filter_horizontal = ('speakers',)
    formfield_overrides = {
        models.TimeField: {'widget': TimeInput(attrs={'type': 'time', 'step': 60})}
    }
    formats = [CSV]


# ----------------------------
# EventDay Admin with inline Events + Import/Export
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
class EventDayAdmin(ImportExportModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    inlines = [EventInline]
    formats = [CSV]


# ----------------------------
# Speaker Admin with Import/Export
# ----------------------------
@admin.register(Speaker)
class SpeakerAdmin(ImportExportModelAdmin):
    resource_class = SpeakerResource  # link the resource
    list_display = ('name', 'designation', 'organization')
    search_fields = ('name', 'organization', 'designation')
    formats = [CSV]

    # Optional: display small image in admin list
    def photo_thumbnail(self, obj):
        if obj.photo:
            return f'<img src="{obj.photo.url}" style="height:50px;"/>'
        return "-"
    photo_thumbnail.short_description = 'Photo'
    photo_thumbnail.allow_tags = True
