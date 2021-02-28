from django.urls import path
from mainapp.views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

