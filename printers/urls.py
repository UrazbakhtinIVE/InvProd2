from django.urls import path
from printers.views import *

urlpatterns = [
    path('', PrinterTemplate.as_view(), name='printer_template'),
    path('list/',PrinterList.as_view(),name='printer_list'),
    path('create/',PrinterCreate.as_view(), name='printer_create'),
    path('update/<int:pk>',PrinterUpdate.as_view(), name='printer_update'),
    path('detail/<int:pk>/', PrinterDetail.as_view(),name='printer_detail'),
    path('scheduler_list/', PrinterSchedulerList.as_view(), name='printer_scheduler_list'),
    path('create_scheduler/', PrinterShedulerCreate.as_view(), name='create_printer_scheduler'),
]

