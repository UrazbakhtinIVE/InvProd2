from django.contrib.auth.decorators import login_required
from django.urls import path
from devices.views import (
    DevicesView, DevicesListView, AddDeviceFromCategory,
    AddMonitorView, AddHeadsetView, AddSpeakerView, UpdateMonitorView, DevicesSchedulerListView, MonitorDetailedView, MonitorDelete
)
from printers.views import PrinterCreateView


urlpatterns = [
    path('', DevicesView.as_view(), name='devices_info'),
    path('list/', DevicesListView.as_view(), name='output_list'),
    path('sheduler_list', DevicesSchedulerListView.as_view(), name='devices_sheduler_list'),
    path('crate_template/', AddDeviceFromCategory.as_view(), name='devicesCreateTemplateView'),
    path('create_monitor/', AddMonitorView.as_view(), name="createMonitor"),
    path('update_monitor/<int:pk>/', UpdateMonitorView.as_view(), name='updateMonitor'),
    path('monitor_detile/<int:pk>/', MonitorDetailedView.as_view(), name='monitorDetile'),
    path('monitor_delete/<int:pk>/', MonitorDelete.as_view(), name='monitorDelete'),
    path('create_headset/', AddHeadsetView.as_view(), name="createHeadset"),
    path('create_speaker/', AddSpeakerView.as_view(), name="createSpeaker"),

]
