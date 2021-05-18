from django.urls import path

from . import views

urlpatterns = [
    path("printer_scheduler_list/", views.PrinterSchedulerListView.as_view(), name="printer_scheduler_list"),
    path("cartridge_scheduler_list/", views.CartridgeSchedulerListView.as_view(), name="cartridge_scheduler_list"),
    path("monitor_scheduler_list/", views.MonitorSchedulerListView.as_view(), name="monitor_scheduler_list"),
    path("headset_scheduler_list/", views.HeadsetSchedulerListView.as_view(), name="headset_scheduler_list"),
    path("speakers_scheduler_list/", views.SpeakersSchedulerListView.as_view(), name="speakers_scheduler_list"),
    path("output_scheduler_list/", views.OutputDevicesSchedulerListView.as_view(), name="output_scheduler_list"),
]
