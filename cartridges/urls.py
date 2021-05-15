from django.urls import path

from cartridges.views import (
    CartridgeInfo, CartridgeListView, CartridgeDetailView, CartridgeCreateView,
    CartridgeUpdateView, CartridgeDelete
)


urlpatterns = [
    path('list/', CartridgeListView.as_view(), name='cartridge_list'),
    path('detail/<int:pk>/', CartridgeDetailView.as_view(), name='cartridge_detail'),
    path('cartridge_info/', CartridgeInfo.as_view(), name='cartridge_info'),
    path('create/', CartridgeCreateView.as_view(), name='create_cartridge'),
    path('update/<int:pk>/', CartridgeUpdateView.as_view(), name='update_cartridge'),
    path('delete/<int:pk>/', CartridgeDelete.as_view(), name='delete_cartridge')
]
