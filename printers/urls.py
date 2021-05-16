from django.urls import path

from mainapp.views import PrintView
from printers.views import (
    PrinterInfo, PrinterListView, PrinterCreateView,
    PrinterUpdateView, PrinterDetailView,
    PrinterAnalyticsListView,
    BlackCartridgesAutocomplete,
    BlueCartridgesAutocomplete,
    YellowCartridgesAutocomplete,
    PurpleCartridgesAutocomplete,
    PrinterAnalytics,
    PrinterAnalyzUpdateView
)


urlpatterns = [
    path('print_info/', PrintView.as_view(), name='printer_template'),
    path('printer_info/', PrinterInfo.as_view(), name='printer_info'),
    path('list/', PrinterListView.as_view(), name='printer_list'),
    path('create/', PrinterCreateView.as_view(), name='printer_create'),
    path('update/<int:pk>', PrinterUpdateView.as_view(), name='printer_update'),
    path('detail/<int:pk>/', PrinterDetailView.as_view(),name='printer_detail'),
    path('diagnostics_list/', PrinterAnalyticsListView.as_view(), name="diagnostics_list"),
    path('black-cartridges-autocomplete/',
         BlackCartridgesAutocomplete.as_view(), name='black-cartridges-autocomplete'),
    path('blue-cartridges-autocomplete/',
         BlueCartridgesAutocomplete.as_view(), name='blue-cartridges-autocomplete'),
    path('yellow-cartridges-autocomplete/',
         YellowCartridgesAutocomplete.as_view(), name='yellow-cartridges-autocomplete'),
    path('purple-cartridges-autocomplete/',
         PurpleCartridgesAutocomplete.as_view(), name='purple-cartridges-autocomplete'),
    path('analytics/', PrinterAnalytics.as_view(), name='printerAnalytics'),

    path('printer_analyz_update/<int:pk>/', PrinterAnalyzUpdateView.as_view(), name='printer_analyz_update')
]

