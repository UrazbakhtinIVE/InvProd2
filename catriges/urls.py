from django.urls import path
from catriges.views import *

urlpatterns = [
    path('list/', CatrigeListView.as_view(), name='catrige_list'),
    path('detile/<int:pk>/', CatrigeDetailView.as_view(), name='catrige_detile'),
    path('create/', CatrigeCreateView.as_view(), name='create_catrige'),
    path('schedulerList/', CatrigeSchedulerListView.as_view(), name='catrige_scheduler_list')

]

