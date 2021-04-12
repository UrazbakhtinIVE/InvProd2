from itertools import chain

from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from outputs.models import Monitor, Headset, Speakers


class OutputsView(TemplateView):
    template_name = 'outputs/outputs_info.html'


class OutputsList(LoginRequiredMixin, ListView):
    """Представление, выводящие все устройства."""

    monitors = Monitor.objects.all()
    headsets = Headset.objects.all()
    speakers = Speakers.objects.all()
    queryset = chain(monitors, headsets, speakers)
    
    template_name = 'outputs/outputsList.html'