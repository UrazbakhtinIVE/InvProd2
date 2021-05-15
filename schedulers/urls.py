from django.urls import path

from .views import (
    PrinterSchedulerListView, CartridgeSchedulerListView, DevicesSchedulerListView
)

urlpatterns = [
    path("printer_scheduler_list/", PrinterSchedulerListView.as_view(), name="printer_scheduler_list"),
    path("cartridge_scheduler_list/", CartridgeSchedulerListView.as_view(), name="cartridge_scheduler_list"),
    path("devices_scheduler_list/", DevicesSchedulerListView.as_view(), name="devices_scheduler_list"),
]
