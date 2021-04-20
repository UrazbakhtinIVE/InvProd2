from django.contrib import admin

from outputs.models import *


@admin.register(MonitorModel)
class MonitorModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ['serialNumber']


@admin.register(HeadsetModel)
class HeadsetModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Headset)
class HeadsetAdmin(admin.ModelAdmin):
    list_display = ['serialNumber']

@admin.register(SpeakersModel)
class SpeakersModelAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Speakers)
class SpeakersAdmin(admin.ModelAdmin):
    list_display = ['serialNumber']


@admin.register(StatusOutputs)
class  StatusOutputsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(MonitorScheduler)
class MonitorSchedulerAdmin(admin.ModelAdmin):
    list_display = ['monitor','monitorStatus','person', 'location','date']






