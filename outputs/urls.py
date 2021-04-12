from django.urls import path
from outputs.views import OutputsView, OutputsList


urlpatterns = [
    path('', OutputsView.as_view(), name='outputs_info'),
    path('list/', OutputsList.as_view(), name='output_list'),

]
