from django.urls import path
from catriges.views import *

urlpatterns = [
    path('list/', CatrigeListView.as_view(), name='catrige_list'),
]

