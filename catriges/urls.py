from django.urls import path
from catriges.views import *

urlpatterns = [
    path('list/', CatrigeListView.as_view(), name='catrige_list'),
    path('detile/<int:pk>/', CatrigeDetailView.as_view(), name='catrige_detile'),
    path('create/', CatrigeCreateView.as_view(), name='create_catrige'),
    path('update/<int:pk>/', CatrigeUpdateView.as_view(), name='update_catrige'),
    path('delete/<int:pk>/', CatrigeDelete.as_view(), name='delete_catrige'),
    path('schedulerList/', CatrigeSchedulerListView.as_view(), name='catrige_scheduler_list')


]

