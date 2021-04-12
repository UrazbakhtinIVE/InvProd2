from django.shortcuts import render
from django.views.generic import *

from outputs.models import *


class OutputsView(TemplateView):
    template_name = 'outputs/outputs_info.html'



class HeadsetList(ListView):
    model = Headset
    queryset = Headset.objects.all()
    template_name = 'outputs/outputsList.html'
    context_object_name = 'headSet'


class MonitorList(ListView):
    model = Monitor
    queryset = Monitor.objects.all()
    template_name = 'outputs/outputsList.html'
    context_object_name = 'monitor'


    def get_context_data(self, **kwargs):
        complex = super(MonitorList, self).get_context_data()
