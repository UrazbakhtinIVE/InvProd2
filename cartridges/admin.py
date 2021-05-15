from django.contrib import admin

from cartridges.models import CartridgeModel, Cartridge


@admin.register(CartridgeModel)
class CartridgeModelModelAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'color', 'firm']

@admin.register(Cartridge)
class CartridgeModelAdmin(admin.ModelAdmin):
    list_display = ['serialNumber', 'model', 'status']