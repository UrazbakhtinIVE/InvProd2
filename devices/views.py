import datetime
import itertools

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (
    ListView, TemplateView, FormView, CreateView,
    UpdateView, DetailView, DeleteView
)
from django.urls import reverse_lazy
from django.views.generic.base import View

from mainapp.models import Category, PeriodOfDiagnostics
from .models import Monitor, Headset, Speakers
from .forms import (
    DevicesCategoriesForm, MonitorUpdateForm,
    MonitorCreateForm, HeadsetForm)

class DevicesView(TemplateView):
    template_name = 'devices/devices_info.html'


class OutputDevicesListView(LoginRequiredMixin, View):
    """Представление, выводящие все устройства вывода."""

    def get_queryset(self, params):
        _serial_number = params.get("serialNumber")
        _control_period_pk = params.get("control_period")

        monitors = Monitor.objects.all()
        headsets = Headset.objects.all()
        speakers = Speakers.objects.all()

        if _serial_number:
            monitors = monitors.filter(serialNumber__icontains=_serial_number)
            headsets = headsets.filter(serialNumber__icontains=_serial_number)
            speakers = speakers.filter(serialNumber__icontains=_serial_number)

        if _control_period_pk:
            control_period = PeriodOfDiagnostics.objects.get(pk=_control_period_pk)
            now = datetime.date.today()

            def filter_instance(instance):
                """период диагностики + дата последней диагностики
                    < текущая дата + контрольный период диагностики
                """
                if (instance.period_of_product_diagnostics.period
                        + instance.date_of_last_diagnostics
                        < now + control_period.period):
                    return instance

            return filter(
                lambda instance: filter_instance(instance),
                itertools.chain(monitors, headsets, speakers)
            )
        return itertools.chain(monitors, headsets, speakers)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset(params=request.GET)

        context = {
            "devices": queryset,
            "control_periods": PeriodOfDiagnostics.objects.all()
        }
        return render(request, 'devices/devicesList.html', context)


class AddDeviceFromCategory(FormView):
    queryset = Category.objects.all()
    template_name = 'devices/devicesCreateTemplate.html'
    form_class = DevicesCategoriesForm


class AddMonitorView(CreateView):
    model = Monitor
    template_name = "devices/createMonitor.html"
    form_class = MonitorCreateForm
    success_url = reverse_lazy("device_list")


class UpdateMonitorView(UpdateView):
    model = Monitor
    form_class = MonitorUpdateForm
    template_name = 'devices/updateMonitor.html'
    context_object_name = 'um'


class MonitorDetailedView(DetailView):
    model = Monitor
    queryset = Monitor.objects.all()
    template_name = 'devices/detileMonitor.html'
    context_object_name = 'md'


class MonitorDelete(DeleteView):
    model = Monitor
    template_name = 'devices/monitorDelete.html'
    context_object_name = 'md'
    success_url = reverse_lazy('device_list')




class DevicesSchedulerListView(ListView):
    """Представление, выводящие все устройства в журнале."""

    # def get(self, request, *args, **kwargs):
    #     monitors = MonitorScheduler.objects.all()
    #     printers = PrinterScheduler.objects.all()
    #     # headsets = Headset.objects.all()
    #     # speakers = Speakers.objects.all()
    #
    #     comntext = {
    #         "monitors": monitors,
    #         'printers': printers,
    #         # "headsets": headsets,
    #         # "speakers": speakers
    #     }
    #     return render(request, 'devices/devicesShedulerList.html', comntext)


class AddHeadsetView(CreateView):
    model = Headset
    template_name = "devices/createHeadset.html"
    form_class = HeadsetForm
    success_url = reverse_lazy("device_list")


class AddSpeakerView(CreateView):
    model = Speakers
    template_name = "devices/createSpeaker.html"
    fields = "__all__"
    success_url = reverse_lazy("device_list")
