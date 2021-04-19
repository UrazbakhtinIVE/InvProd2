from django.contrib import admin
from printers.models import *


@admin.register(PrinterModel)
class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'printerType', 'category']


@admin.register(PrinterType)
class PrinterTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['serialNumber','printerModel','name','ip','status']
    search_fields = ['serialNumber']


@admin.register(PrinterStatus)
class PrinterStatusAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(PrinterScheduler)
class PrinterSchedulerAdmin(admin.ModelAdmin):
    list_display = ['uuid','printer','printerStatus','date']



