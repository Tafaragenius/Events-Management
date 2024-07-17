# admin.py

from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'start_time', 'finish_time', 'venue')
    search_fields = ('title', 'user__username', 'venue')

admin.site.register(Event, EventAdmin)


