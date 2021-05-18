from django.urls import path

from . import views


urlpatterns = [
    path('', views.Wellcome.as_view(), name='wellcome'),
    path('home/', views.IndexView.as_view(), name='index'),

    path('home/devices_info/', views.InfoView.as_view(), name='devices_info'),
    path('home/devices_output_info/', views.OutputsDevicesInfoView.as_view(), name='devices_outputs_info'),
    path('home/devices_input_info/', views.InputsDevicesInfoView.as_view(), name='devices_inputs_info'),
    path('home/devices_other_info/', views.OthersDevicesInfoView.as_view(), name='devices_others_info'),

    path('export_printer_analytics', views.ExportPrinterAnalytics.as_view(), name='export_printer_analytics'),
    path('export_cartridge_analytics', views.ExportCartridgeAnalytics.as_view(), name='export_cartridge_analytics'),
    path('export_monitor_analytics', views.ExportMonitorAnalytics.as_view(), name='export_monitor_analytics'),
    path('export_headset_analytics', views.ExportHeadsetAnalytics.as_view(), name='export_headset_analytics'),
    path('export_speakers_analytics', views.ExportSpeakersAnalytics.as_view(), name='export_speakers_analytics'),
    path('export_output_devices_analytics', views.ExportOutputDevicesAnalytics.as_view(), name='export_output_devices_analytics')
]

