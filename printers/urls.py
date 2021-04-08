from django.urls import path
from printers.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('printer_info/', login_required(PrinterInfo.as_view()), name='printer_info'),
    path('list/', login_required(PrinterListView.as_view()), name='printer_list'),
    path('create/', login_required(PrinterCreateView.as_view()), name='printer_create'),
    path('update/<int:pk>',login_required(PrinterUpdateView.as_view()), name='printer_update'),
    path('detail/<int:pk>/', login_required(PrinterDetailView.as_view()),name='printer_detail'),
    path('scheduler_list/', login_required(PrinterSchedulerListView.as_view()), name='printer_scheduler_list'),
    path('create_scheduler/', login_required(PrinterShedulerCreateView.as_view()), name='create_printer_scheduler'),
    path('black-cartridges-autocomplete/',
         BlackCartridgesAutocomplete.as_view(), name='black-cartridges-autocomplete'),
    path('blue-cartridges-autocomplete/',
         BlueCartridgesAutocomplete.as_view(), name='blue-cartridges-autocomplete'),
    path('yellow-cartridges-autocomplete/',
         YellowCartridgesAutocomplete.as_view(), name='yellow-cartridges-autocomplete'),
    path('purple-cartridges-autocomplete/',
         PurpleCartridgesAutocomplete.as_view(), name='purple-cartridges-autocomplete'),
]

