from itertools import chain
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.views.generic import ListView, TemplateView, FormView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.base import View

from outputs.models import Monitor, Headset, Speakers,MonitorScheduler
from mainapp.models import Category
from .forms import OutputsCategoriesForm, MonitorUpdateForm, MonitorCreateForm
from printers.models import Printer


class OutputsView(TemplateView):
    template_name = 'outputs/outputs_info.html'



class OutputsListView(LoginRequiredMixin, View):
    """Представление, выводящие все устройства."""

    def get(self, request, *args, **kwargs):
        monitors = Monitor.objects.all()
        headsets = Headset.objects.all()
        speakers = Speakers.objects.all()
        printers = Printer.objects.all()

        comntext = {
            "monitors": monitors,
            "headsets": headsets,
            "speakers": speakers,
            "printers": printers

        }
        return render(request, 'outputs/outputsList.html', comntext)


class AddOutputFromCategory(FormView):
    queryset = Category.objects.all()
    template_name = 'outputs/outputsCreateTemplate.html'
    form_class = OutputsCategoriesForm


class AddMonitorView(CreateView):
    model = Monitor
    template_name = "outputs/createMonitor.html"
    form_class = MonitorCreateForm
    success_url = reverse_lazy("output_list")


class UpdateMonitorView(UpdateView):
    model = Monitor
    form_class = MonitorUpdateForm
    template_name = 'outputs/updateMonitor.html'
    context_object_name = 'um'
    # success_url = 'outputs/'



class OutputsShedulerListView(ListView):
    """Представление, выводящие все устройства."""

    def get(self, request, *args, **kwargs):
        monitors = MonitorScheduler.objects.all()
        # headsets = Headset.objects.all()
        # speakers = Speakers.objects.all()

        comntext = {
            "monitors": monitors,
            # "headsets": headsets,
            # "speakers": speakers
        }
        return render(request, 'outputs/outputsShedulerList.html', comntext)



class AddHeadsetView(CreateView):
    model = Headset
    template_name = "outputs/createHeadset.html"
    fields = "__all__"
    success_url = reverse_lazy("output_list")


class AddSpeakerView(CreateView):
    model = Speakers
    template_name = "outputs/createSpeaker.html"
    fields = "__all__"
    success_url = reverse_lazy("output_list")
