import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (
    TemplateView, FormView, CreateView,
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
    template_name = "devices/devices_info.html"


class OutputDevicesListView(LoginRequiredMixin, View):
    """Представление, выводящие все устройства вывода."""

    def get_queryset(self, params):
        _serial_number = params.get("serialNumber", "")
        _control_period_pk = params.get("control_period")

        monitors = Monitor.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model")
        headsets = Headset.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model")
        speakers = Speakers.objects \
            .filter(serialNumber__icontains=_serial_number)\
            .select_related("model")

        if _control_period_pk:
            control_period = PeriodOfDiagnostics.objects.get(pk=_control_period_pk)
            now = datetime.date.today()

            def filter_instance(instance):
                """период диагностики + дата последней диагностики
                    < текущая дата + контрольный период диагностики
                """
                if not instance.period_of_product_diagnostics:
                    return
                if (instance.period_of_product_diagnostics.period
                        + instance.date_of_last_diagnostics
                        < now + control_period.period):
                    return instance
            return {
                "monitors": filter(
                    lambda instance: filter_instance(instance),
                    monitors.iterator()
                ),
                "headsets": filter(
                    lambda instance: filter_instance(instance),
                    headsets.iterator()
                ),
                "speakers": filter(
                    lambda instance: filter_instance(instance),
                    speakers.iterator()
                )
            }
        return {
            "monitors": monitors.iterator(),
            "headsets": headsets.iterator(),
            "speakers": speakers.iterator()
        }

    def get(self, request, *args, **kwargs):
        devices = self.get_queryset(params=request.GET)
        total_count = Monitor.objects.count() \
                      + Headset.objects.count() \
                      + Speakers.objects.count()

        context = {
            **devices,
            "total_count": total_count,
            "control_periods": PeriodOfDiagnostics.objects.all()
        }
        return render(request, "devices/output_devices_list.html", context)


class AddDeviceFromCategory(FormView):
    queryset = Category.objects.all()
    template_name = "devices/devices_create.html"
    form_class = DevicesCategoriesForm


class AddMonitorView(CreateView):
    model = Monitor
    template_name = "devices/monitor_create.html"
    form_class = MonitorCreateForm
    success_url = reverse_lazy("output_list")


class MonitorDetailedView(DetailView):
    model = Monitor
    queryset = Monitor.objects.all()
    template_name = "devices/monitor_detail.html"
    context_object_name = "md"


class UpdateMonitorView(UpdateView):
    model = Monitor
    form_class = MonitorUpdateForm
    template_name = "devices/monitor_update.html"
    context_object_name = "um"


class MonitorDelete(DeleteView):
    model = Monitor
    template_name = "devices/monitor_delete.html"
    context_object_name = "md"
    success_url = reverse_lazy("output_list")


class AddHeadsetView(CreateView):
    model = Headset
    template_name = "devices/headset_create.html"
    form_class = HeadsetForm
    success_url = reverse_lazy("output_list")


class AddSpeakerView(CreateView):
    model = Speakers
    template_name = "devices/speakers_create.html"
    fields = "__all__"
    success_url = reverse_lazy("output_list")
