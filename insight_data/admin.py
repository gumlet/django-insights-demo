from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']
    list_display = ['name', 'playback_id', 'playback_time_instant', 'created_at']

admin.site.register(Event, EventAdmin)