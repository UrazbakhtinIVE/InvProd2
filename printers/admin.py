from django.contrib import admin
from printers.models import PrinterModel, PrinterType, PrinterStatus, Printer


@admin.register(PrinterModel)
class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'category']


@admin.register(PrinterType)
class PrinterTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['serialNumber', 'model', 'name', 'ip', 'status']
    search_fields = ['serialNumber']


@admin.register(PrinterStatus)
class PrinterStatusAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}



