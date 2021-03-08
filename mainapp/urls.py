from django.urls import path
from mainapp.views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('info/', PrinterTemplate.as_view(), name='printer_template'),
]

