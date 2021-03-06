from django.contrib.auth.decorators import login_required
from django.urls import path
from outputs.views import (
    OutputsView, OutputsListView, AddOutputFromCategory,
    AddMonitorView, AddHeadsetView, AddSpeakerView, UpdateMonitorView, OutputsSchedulerListView, MonitorDetailedView, MonitorDelete
)
from printers.views import PrinterCreateView


urlpatterns = [
    path('', OutputsView.as_view(), name='outputs_info'),
    path('list/', OutputsListView.as_view(), name='output_list'),
    path('sheduler_list', OutputsSchedulerListView.as_view(), name='outputs_sheduler_list'),
    path('crate_template/', AddOutputFromCategory.as_view(), name='outputsCreateTemplateView'),
    path('create_monitor/', AddMonitorView.as_view(), name="createMonitor"),
    path('update_monitor/<int:pk>/', UpdateMonitorView.as_view(), name='updateMonitor'),
    path('monitor_detile/<int:pk>/', MonitorDetailedView.as_view(), name='monitorDetile'),
    path('monitor_delete/<int:pk>/', MonitorDelete.as_view(), name='monitorDelete'),
    path('create_headset/', AddHeadsetView.as_view(), name="createHeadset"),
    path('create_speaker/', AddSpeakerView.as_view(), name="createSpeaker"),

]
