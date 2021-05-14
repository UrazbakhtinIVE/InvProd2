from django.urls import path
from devices.views import (
    DevicesView, OutputDevicesListView, AddDeviceFromCategory,
    AddMonitorView, AddHeadsetView, AddSpeakerView, UpdateMonitorView,
    DevicesSchedulerListView, MonitorDetailedView, MonitorDelete
)

urlpatterns = [
    path('', DevicesView.as_view(), name='devices_info'),
    path('output/list/', OutputDevicesListView.as_view(), name='output_list'),
    path('sheduler_list', DevicesSchedulerListView.as_view(), name='devices_sheduler_list'),
    path('crate_template/', AddDeviceFromCategory.as_view(), name='devicesCreateTemplateView'),
    path('create_monitor/', AddMonitorView.as_view(), name="createMonitor"),
    path('update_monitor/<int:pk>/', UpdateMonitorView.as_view(), name='updateMonitor'),
    path('monitor_detile/<int:pk>/', MonitorDetailedView.as_view(), name='monitorDetile'),
    path('monitor_delete/<int:pk>/', MonitorDelete.as_view(), name='monitorDelete'),
    path('create_headset/', AddHeadsetView.as_view(), name="createHeadset"),
    path('create_speaker/', AddSpeakerView.as_view(), name="createSpeaker"),
]
