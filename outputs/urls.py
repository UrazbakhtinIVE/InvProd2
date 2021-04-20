from django.urls import path
from outputs.views import (
    OutputsView, OutputsListView, AddOutputFromCategory,
    AddMonitorView, AddHeadsetView, AddSpeakerView,UpdateMonitorView, OutputsShedulerListView,
)


urlpatterns = [
    path('', OutputsView.as_view(), name='outputs_info'),
    path('list/', OutputsListView.as_view(), name='output_list'),
    path('sheduler_list', OutputsShedulerListView.as_view(),name='outputs_sheduler_list' ),
    path('crate_template/', AddOutputFromCategory.as_view(), name='outputsCreateTemplateView'),
    path('create_monitor/', AddMonitorView.as_view(), name="createMonitor"),
    path('update_monitor/<int:pk>/', UpdateMonitorView.as_view(), name='updateMonitor'),
    path('create_headset/', AddHeadsetView.as_view(), name="createHeadset"),
    path('create_speaker/', AddSpeakerView.as_view(), name="createSpeaker"),
]
