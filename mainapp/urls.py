from django.urls import path
from mainapp.views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('output/', InfoView.as_view(), name='output'),
]

