from django.urls import path
from mainapp.views import (
    IndexView, InfoView, Wellcome,
    OutputsDevicesInfoView, InputsDevicesInfoView, OthersDevicesInfoView,
    ExportPrintersAnalytics,
    ExportCartridgeAnalytics,
    ExportOutputDevicesAnalytics
)


urlpatterns = [
    path('', Wellcome.as_view(), name='wellcome'),
    path('home/', IndexView.as_view(), name='index'),
    path('home/devices_info/', InfoView.as_view(), name='devices_info'),
    path('home/devices_outputs_info/', OutputsDevicesInfoView.as_view(), name='devices_outputs_info'),
    path('home/devices_inputs_info/', InputsDevicesInfoView.as_view(), name='devices_inputs_info'),
    path('home/devices_others_info/', OthersDevicesInfoView.as_view(), name='devices_others_info'),
    path('export_printers_analytics', ExportPrintersAnalytics.as_view(), name='export_printers_analytics'),
    path('export_cartridges_analytics', ExportCartridgeAnalytics.as_view(), name='export_cartridges_analytics'),
    path('export_output_devices_analytics', ExportOutputDevicesAnalytics.as_view(), name='export_output_devices_analytics'),
]

