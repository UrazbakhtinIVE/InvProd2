from django.urls import path
from catriges.views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('list/', login_required(CatrigeListView.as_view()), name='catrige_list'),
    path('detile/<int:pk>/', login_required(CatrigeDetailView.as_view()), name='catrige_detile'),
    path('create/', login_required(CatrigeCreateView.as_view()), name='create_catrige'),
    path('update/<int:pk>/', login_required(CatrigeUpdateView.as_view()), name='update_catrige'),
    path('delete/<int:pk>/', login_required(CatrigeDelete.as_view()), name='delete_catrige'),
    path('schedulerList/', login_required(CatrigeSchedulerListView.as_view()), name='catrige_scheduler_list'),
    path('search-first-name-autocomplete/', SearchFirstNameAutocomplete.as_view(),name='search-first-name-autocomplete')
]

