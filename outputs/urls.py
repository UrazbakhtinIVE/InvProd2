from django.urls import path
from outputs.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(OutputsView.as_view()),         name='outputs_info'),
    path('list/', login_required(MonitorList.as_view()), name='output_list'),
    path('list/', login_required(HeadsetList.as_view()), name='output_list'),

]
