from django.contrib import admin

from .models import (
    PrinterScheduler,
    CartridgeScheduler,
    MonitorScheduler,
    SpeakersScheduler,
    HeadsetScheduler
)


@admin.register(PrinterScheduler)
class PrinterScheduler(admin.ModelAdmin):
    list_display = ("printer", "date", "status")

@admin.register(CartridgeScheduler)
class CartridgeScheduler(admin.ModelAdmin):
    list_display = ("cartridge", "date", "status")

@admin.register(MonitorScheduler)
class MonitorScheduler(admin.ModelAdmin):
    list_display = ("monitor", "date", "status")

@admin.register(SpeakersScheduler)
class SpeakersScheduler(admin.ModelAdmin):
    list_display = ("speakers", "date", "status")

@admin.register(HeadsetScheduler)
class HeadsetScheduler(admin.ModelAdmin):
    list_display = ("headset", "date", "status")