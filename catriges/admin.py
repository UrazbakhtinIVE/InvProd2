from django.contrib import admin
from catriges.models import *


@admin.register(CartridgeModel)
class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ['category','name','color', 'firm']

@admin.register(CatrigeStatus)
class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Catrige)
class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ['catrigeModel','status']



@admin.register(CatrigeScheduler)
class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ['uuid','catrige','catrigeStatus']



