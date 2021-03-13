from django.urls import path
from catriges.views import *

urlpatterns = [
    path('list/', CatrigeListView.as_view(), name='catrige_list'),
    path('create/', CatrigeCreateView.as_view(), name='create_catrige'),
    path('catrigeSchedulerList/', CatrigeSchedulerListView.as_view(), name='catrige_scheduler_list')

]

