from django.contrib import admin

from devices.models import (
    MonitorModel, HeadsetModel, SpeakersModel,
    Monitor, Headset, Speakers
)


@admin.register(MonitorModel)
class MonitorModelAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(HeadsetModel)
class HeadsetModelAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(SpeakersModel)
class SpeakersModelAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ["serialNumber", "model", "status"]


@admin.register(Headset)
class HeadsetAdmin(admin.ModelAdmin):
    list_display = ["serialNumber", "model", "status"]


@admin.register(Speakers)
class SpeakersAdmin(admin.ModelAdmin):
    list_display = ["serialNumber", "model", "status"]





