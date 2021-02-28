from django.contrib import admin
from locations.models import *


@admin.register(Tituls)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number', 'name']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number', 'titul']

