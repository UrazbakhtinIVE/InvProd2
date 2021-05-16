from django.urls import path
from devices.views import (
    DevicesView, OutputDevicesListView, AddDeviceFromCategory,
    AddMonitorView, AddHeadsetView, AddSpeakerView, UpdateMonitorView,
    MonitorDetailedView, MonitorDelete, OutputDevicesInfoView, OutputDevicesAnalyticsListView, MonitorTemplateView,
    ListMonitorView, DetailMonitorView, HeaderSetTemplateView, SpeakersTemplateView
)

urlpatterns = [
    path('', DevicesView.as_view(), name='devices_info'),
    path('output/info/', OutputDevicesInfoView.as_view(), name='output_info'),
    path('output/list/', OutputDevicesListView.as_view(), name='output_list'),
    path('output/analytics/', OutputDevicesAnalyticsListView.as_view(), name='output_analytics'),
    path('create_device/', AddDeviceFromCategory.as_view(), name='devicesCreateTemplateView'),
    path('monitor_info/', MonitorTemplateView.as_view(), name='monitor_info'),
    path('monitor_list/', ListMonitorView.as_view(), name='monitor_list'),

    # path('monitor_detail/<pk:int>/', DetailMonitorView.as_view(), name='monitor_detail'),

    path('create_monitor/', AddMonitorView.as_view(), name="createMonitor"),
    path('update_monitor/<int:pk>/', UpdateMonitorView.as_view(), name='updateMonitor'),
    path('monitor_detail/<int:pk>/', MonitorDetailedView.as_view(), name='monitorDetail'),
    path('monitor_delete/<int:pk>/', MonitorDelete.as_view(), name='monitorDelete'),
    path('create_headset/', AddHeadsetView.as_view(), name="createHeadset"),
    path('headrest_info/', HeaderSetTemplateView.as_view(), name='headrest_info'),
    path('speakers_info/', SpeakersTemplateView.as_view(), name='speakers_info'),


    path('create_speaker/', AddSpeakerView.as_view(), name="createSpeaker"),
]
