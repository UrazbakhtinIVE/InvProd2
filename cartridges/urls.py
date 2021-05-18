from django.urls import path

from . import views


urlpatterns = [
    path("info/", views.CartridgeInfoView.as_view(), name="cartridge_info"),
    path("create/", views.CartridgeCreateView.as_view(), name="cartridge_create"),
    path("list/", views.CartridgeListView.as_view(), name="cartridge_list"),
    path("detail/<int:pk>/", views.CartridgeDetailView.as_view(), name="cartridge_detail"),
    path("update/<int:pk>/", views.CartridgeUpdateView.as_view(), name="cartridge_update"),
    path("delete/<int:pk>/", views.CartridgeDelete.as_view(), name="cartridge_delete"),
    path("analytics/", views.CartridgeAnalyticsListView.as_view(), name="cartridge_analytics_list"),
    path("analytics/update/<int:pk>/", views.CartridgeAnalyticsUpdateView.as_view(), name="cartridge_analytics_update"),
]
