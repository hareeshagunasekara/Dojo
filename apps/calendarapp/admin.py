from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'start_date', 'start_time', 'event_type', 'created_at']
    list_filter = ['event_type', 'start_date', 'user']
    search_fields = ['title', 'description', 'location']
    date_hierarchy = 'start_date'
    ordering = ['start_date', 'start_time']
