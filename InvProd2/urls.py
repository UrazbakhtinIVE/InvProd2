from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('printer/', include('printers.urls')),
    path("select2/", include("django_select2.urls")),
]
