from django.urls import path
from printers.views import *

urlpatterns = [
    path('list/',PrinterListView.as_view(),name='printer_list'),
    path('create/',PrinterCreateView.as_view(), name='printer_create'),
    path('update/<int:pk>',PrinterUpdateView.as_view(), name='printer_update'),
    path('detail/<int:pk>/', PrinterDetailView.as_view(),name='printer_detail'),
    path('scheduler_list/', PrinterSchedulerListView.as_view(), name='printer_scheduler_list'),
    path('create_scheduler/', PrinterShedulerCreateView.as_view(), name='create_printer_scheduler'),
    path('black-cartridges-autocomplete/',
         BlackCartridgesAutocomplete.as_view(), name='black-cartridges-autocomplete'),
    path('blue-cartridges-autocomplete/',
         BlueCartridgesAutocomplete.as_view(), name='blue-cartridges-autocomplete'),
    path('yellow-cartridges-autocomplete/',
         YellowCartridgesAutocomplete.as_view(), name='yellow-cartridges-autocomplete'),
    path('purple-cartridges-autocomplete/',
         PurpleCartridgesAutocomplete.as_view(), name='purple-cartridges-autocomplete'),
]

