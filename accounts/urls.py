from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path


urlpatterns = [
    path('account/login/', LoginView.as_view(), name='login'),
    path('account/logout/', LogoutView.as_view(next_page='/'), name='logout')
]