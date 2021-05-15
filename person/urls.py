from django.urls import path

from cartridges.views import SearchFirstNameAutocomplete

urlpatterns = [
    path('search-first-name-autocomplete/', SearchFirstNameAutocomplete.as_view(),name='search-first-name-autocomplete'),
]

