from django.urls import path
from devices.views import (
    DevicesView, OutputDevicesListView, AddDeviceFromCategory,
    AddMonitorView, AddHeadsetView, AddSpeakerView, UpdateMonitorView,
    MonitorDetailedView, MonitorDelete
)

urlpatterns = [
    path('', DevicesView.as_view(), name='devices_info'),
    path('output/list/', OutputDevicesListView.as_view(), name='output_list'),
    path('create_device/', AddDeviceFromCategory.as_view(), name='devicesCreateTemplateView'),
    path('create_monitor/', AddMonitorView.as_view(), name="createMonitor"),
    path('update_monitor/<int:pk>/', UpdateMonitorView.as_view(), name='updateMonitor'),
    path('monitor_detail/<int:pk>/', MonitorDetailedView.as_view(), name='monitorDetail'),
    path('monitor_delete/<int:pk>/', MonitorDelete.as_view(), name='monitorDelete'),
    path('create_headset/', AddHeadsetView.as_view(), name="createHeadset"),
    path('create_speaker/', AddSpeakerView.as_view(), name="createSpeaker"),
]
