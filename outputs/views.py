from itertools import chain
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.views.generic import ListView, TemplateView, FormView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import View

from outputs.models import Monitor, Headset, Speakers, MonitorScheduler
from mainapp.models import Category
from .forms import OutputsCategoriesForm, MonitorUpdateForm, MonitorCreateForm, HeadsetForm
from printers.models import Printer, PrinterScheduler


class OutputsView(TemplateView):
    template_name = 'outputs/outputs_info.html'


class OutputsListView(LoginRequiredMixin, ListView):
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


class MonitorDetailedView(DetailView):
    model = Monitor
    queryset = Monitor.objects.all()
    template_name = 'outputs/detileMonitor.html'
    context_object_name = 'md'


class MonitorDelete(DeleteView):
    model = Monitor
    template_name = 'outputs/monitorDelete.html'
    context_object_name = 'md'
    success_url = reverse_lazy('output_list')




class OutputsSchedulerListView(ListView):
    """Представление, выводящие все устройства в журнале."""

    def get(self, request, *args, **kwargs):
        monitors = MonitorScheduler.objects.all()
        printers = PrinterScheduler.objects.all()
        # headsets = Headset.objects.all()
        # speakers = Speakers.objects.all()

        comntext = {
            "monitors": monitors,
            'printers': printers,
            # "headsets": headsets,
            # "speakers": speakers
        }
        return render(request, 'outputs/outputsShedulerList.html', comntext)


class AddHeadsetView(CreateView):
    model = Headset
    template_name = "outputs/createHeadset.html"
    form_class = HeadsetForm
    success_url = reverse_lazy("output_list")


class AddSpeakerView(CreateView):
    model = Speakers
    template_name = "outputs/createSpeaker.html"
    fields = "__all__"
    success_url = reverse_lazy("output_list")
