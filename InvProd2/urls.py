from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('home/', include('mainapp.urls')),
    path('printer/', include('printers.urls')),
    path('catrige/', include('catriges.urls')),
    path('outputs/', include('outputs.urls')),
    path('person/', include('person.urls')),
    path("select2/", include("django_select2.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


LOGIN_REDIRECT_URL = '/home'
LOGIN_URL = '/'
