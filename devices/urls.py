from django.urls import path

from . import views

urlpatterns = [
    path("", views.OutputDevicesInfoView.as_view(), name="devices_info"),
    path("create/", views.DeviceCreateView.as_view(), name="devices_create"),

    # все устроства вывода
    path("output/info/", views.OutputDevicesInfoView.as_view(), name="output_info"),
    path("output/list/", views.OutputDevicesListView.as_view(), name="output_list"),
    path("output/analytics/", views.OutputDevicesAnalyticsListView.as_view(), name="output_analytics_list"),

    # мониторы
    path("monitor/info/", views.MonitorInfoView.as_view(), name="monitor_info"),
    path("monitor/create/", views.MonitorCreateView.as_view(), name="monitor_create"),
    path("monitor/list/", views.MonitorListView.as_view(), name="monitor_list"),
    path("monitor/<int:pk>/", views.MonitorDetailView.as_view(), name="monitor_detail"),
    path("monitor/update/<int:pk>/", views.MonitorUpdateView.as_view(),  name="monitor_update"),
    path("monitor/delete/<int:pk>/", views.MonitorDeleteView.as_view(), name="monitor_delete"),
    path("monitor/analytics/", views.MonitorAnalyticsListView.as_view(), name="monitor_analytics_list"),
    path("monitor/analytics/update/<int:pk>/", views.MonitorAnalyticsUpdateView.as_view(), name="monitor_analytics_update"),

    # гарнитуры
    path("headset/info/", views.HeadsetInfoView.as_view(), name="headset_info"),
    path("headset/create/", views.HeadsetCreateView.as_view(), name="headset_create"),
    path("headset/list/", views.HeadsetListView.as_view(), name="headset_list"),
    path("headset/<int:pk>/", views.HeadsetDetailView.as_view(), name="headset_detail"),
    path("headset/update/<int:pk>/", views.HeadsetUpdateView.as_view(), name="headset_update"),
    path("headset/delete/<int:pk>/", views.HeadsetDeleteView.as_view(), name="headset_delete"),
    path("headset/analytics/", views.HeadsetAnalyticsListView.as_view(), name="headset_analytics_list"),
    path("headset/analytics/update/<int:pk>/", views.HeadsetAnalyticsUpdateView, name="headset_analytics_update"),

    # колонки
    path("speakers/info/", views.SpeakersInfoView.as_view(), name="speakers_info"),
    path("speakers/create/", views.SpeakersCreateView.as_view(), name="speakers_create"),
    path("speakers/list/", views.SpeakersListView.as_view(), name="speakers_list"),
    path("speakers/<int:pk>/", views.SpeakersDetailView.as_view(), name="speakers_detail"),
    path("speakers/update/<int:pk>/", views.SpeakersUpdateView.as_view(), name="speakers_update"),
    path("speakers/delete/<int:pk>/", views.SpeakersDeleteView.as_view(), name="speakers_delete"),
    path("speakers/analytics/", views.SpeakersAnalyticsListView.as_view(), name="speakers_analytics_list"),
    path("speakers/analytics/update/<int:pk>/", views.SpeakersAnalyticsUpdateView.as_view(), name="speakers_analytics_update"),
]
