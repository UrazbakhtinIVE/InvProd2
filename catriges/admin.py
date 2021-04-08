from django.contrib import admin
from catriges.models import *


@admin.register(CartridgeModel)
class CatrigeModelAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'color', 'firm']


@admin.register(Catrige)
class CatrigeModelAdmin(admin.ModelAdmin):
    list_display = ['serialNumber', 'catrigeModel', 'status']


@admin.register(CatrigeScheduler)
class CatrigeShedulerAdmin(admin.ModelAdmin):
    list_display = ['catrige', 'catrigeStatus', 'date', 'person']
