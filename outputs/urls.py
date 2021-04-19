from django.urls import path
from outputs.views import (
    OutputsView, OutputsListView, AddOutputFromCategory,
    AddMonitorView, AddHeadsetView, AddSpeakerView,
)


urlpatterns = [
    path('', OutputsView.as_view(), name='outputs_info'),
    path('list/', OutputsListView.as_view(), name='output_list'),
    path('crate_template/', AddOutputFromCategory.as_view(), name='outputsCreateTemplateView'),
    path('create_monitor/', AddMonitorView.as_view(), name="createMonitor"),
    path('create_headset/', AddHeadsetView.as_view(), name="createHeadset"),
    path('create_speaker/', AddSpeakerView.as_view(), name="createSpeaker"),
]
