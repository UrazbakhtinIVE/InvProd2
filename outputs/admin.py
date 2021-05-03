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


# @admin.register(StatusOutputs)
# class  StatusOutputsAdmin(admin.ModelAdmin):
#     list_display = ['name']


@admin.register(MonitorScheduler)
class MonitorSchedulerAdmin(admin.ModelAdmin):
    list_display = ['monitor','person', 'location','date']

@admin.register(HeadsetScheduler)
class HeadsetSchedulerAdmin(admin.ModelAdmin):
    list_display = ['headset','person', 'location','date']

@admin.register(SpeakerScheduler)
class SpeakerSchedulerAdmin(admin.ModelAdmin):
    list_display = ['speaker','person', 'location','date']





