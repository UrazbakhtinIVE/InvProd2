import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import (
    TemplateView, FormView, CreateView,
    UpdateView, DetailView, DeleteView, ListView
)
from django.urls import reverse_lazy
from django.views.generic.base import View

from mainapp.models import Category, PeriodOfDiagnostics
from mainapp.utils import filter_by_control_period
from printers.models import Printer
from .models import Monitor, Headset, Speakers
from . import forms


class DeviceCreateView(LoginRequiredMixin, FormView):
    queryset = Category.objects.all()
    template_name = "devices/devices_create.html"
    form_class = forms.DevicesCategoriesForm


class MonitorInfoView(LoginRequiredMixin, TemplateView):
    template_name = "devices/monitor_info.html"


class MonitorCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Monitor
    template_name = "devices/monitor/monitor_create.html"
    success_message = "Новый монитор был успешно создан."
    form_class = forms.MonitorCreateForm
    success_url = reverse_lazy("monitor_list")


class MonitorDetailView(LoginRequiredMixin, DetailView):
    model = Monitor
    template_name = "devices/monitor/monitor_detail.html"


class MonitorListView(LoginRequiredMixin, ListView):
    model = Monitor
    extra_context = {"total_count": Monitor.objects.count()}
    template_name = "devices/monitor/monitor_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        _serial_number = self.request.GET.get("serialNumber", "")
        return queryset \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model")


class MonitorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Monitor
    form_class = forms.MonitorUpdateForm
    template_name = "devices/monitor/monitor_update.html"
    success_message = "Информация о мониторе была успешно обновлена."
    success_url = reverse_lazy("monitor_list")


class MonitorDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Monitor
    template_name = "devices/monitor/monitor_delete.html"
    success_message = "Монитор был успешно удален."
    success_url = reverse_lazy("monitor_list")


class MonitorAnalyticsListView(LoginRequiredMixin, View):
    def get_queryset(self, params):
        _serial_number = params.get("serialNumber", "")
        _control_period_pk = params.get("control_period")

        queryset = Monitor.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model") \
            .order_by("date_of_last_diagnostics")

        if _control_period_pk:
            return filter_by_control_period(period_pk=_control_period_pk, queryset=queryset)
        return queryset.iterator()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset(params=request.GET)
        total_count = Headset.objects.count()

        context = {
            "object_list": queryset,
            "total_count": total_count,
            "control_periods": PeriodOfDiagnostics.objects.all()
        }
        return render(request, "devices/monitor/monitor_analytics_list.html", context)


class MonitorAnalyticsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Monitor
    template_name = "devices/monitor/monitor_analytics_update.html"
    form_class = forms.MonitorAnalyticsUpdateForm
    success_message = "Информация об обслуживании была успешно обновлена."
    success_url = reverse_lazy("monitor_analytics_list")


class HeadsetInfoView(LoginRequiredMixin, TemplateView):
    template_name = "devices/headset_info.html"


class HeadsetCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Headset
    template_name = "devices/headset/headset_create.html"
    form_class = forms.HeadsetCreateForm
    success_message = "Новая гарнитура была успешно создана."
    success_url = reverse_lazy("headset_list")


class HeadsetDetailView(LoginRequiredMixin, DetailView):
    model = Headset
    template_name = "devices/headset/headset_detail.html"


class HeadsetListView(LoginRequiredMixin, ListView):
    model = Headset
    extra_context = {"total_count": Headset.objects.count()}
    template_name = "devices/headset/headset_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        _serial_number = self.request.GET.get("serialNumber", "")
        return queryset \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model")


class HeadsetUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Headset
    form_class = forms.HeadsetUpdateForm
    template_name = "devices/headset/headset_update.html"
    success_message = "Информация о гарнитуре была успешно обновлена."
    success_url = reverse_lazy("headset_list")


class HeadsetDeleteView(LoginRequiredMixin, DeleteView):
    model = Headset
    template_name = "devices/headset/headset_delete.html"
    success_message = "Гарнитура была успешно удалена."
    success_url = reverse_lazy("headset_list")


class HeadsetAnalyticsListView(LoginRequiredMixin, View):
    def get_queryset(self, params):
        _serial_number = params.get("serialNumber", "")
        _control_period_pk = params.get("control_period")

        queryset = Headset.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model") \
            .order_by("date_of_last_diagnostics")

        if _control_period_pk:
            return filter_by_control_period(period_pk=_control_period_pk, queryset=queryset)
        return queryset.iterator()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset(params=request.GET)
        total_count = Headset.objects.count()

        context = {
            "object_list": queryset,
            "total_count": total_count,
            "control_periods": PeriodOfDiagnostics.objects.all()
        }
        return render(request, "devices/headset/headset_analytics_list.html", context)


class HeadsetAnalyticsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Headset
    template_name = "devices/headset/headset_analytics_update.html"
    form_class = forms.HeadsetAnalyticsUpdateForm
    success_url = reverse_lazy("headset_analytics_list")


class SpeakersInfoView(LoginRequiredMixin, TemplateView):
    template_name = "devices/speakers_info.html"


class SpeakersCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Speakers
    template_name = "devices/speakers/speakers_create.html"
    form_class = forms.SpeakersCreateForm
    success_message = "Новые колонки были успешно созданы."
    success_url = reverse_lazy("speakers_list")


class SpeakersDetailView(LoginRequiredMixin, DetailView):
    model = Speakers
    template_name = "devices/speakers/speakers_detail.html"


class SpeakersListView(LoginRequiredMixin, ListView):
    model = Speakers
    extra_context = {"total_count": Speakers.objects.count()}
    template_name = "devices/speakers/speakers_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        _serial_number = self.request.GET.get("serialNumber", "")
        return queryset \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model")


class SpeakersUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Speakers
    form_class = forms.SpeakersUpdateForm
    template_name = "devices/speakers/speakers_update.html"
    success_message = "Информация о колонках была успешно обновлена."
    success_url = reverse_lazy("speakers_list")


class SpeakersDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Speakers
    template_name = "devices/speakers/speakers_delete.html"
    success_message = "Колонки были успешно удалены."
    success_url = reverse_lazy("speakers_list")


class SpeakersAnalyticsListView(LoginRequiredMixin, View):
    def get_queryset(self, params):
        _serial_number = params.get("serialNumber", "")
        _control_period_pk = params.get("control_period")

        queryset = Speakers.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model") \
            .order_by("date_of_last_diagnostics")

        if _control_period_pk:
            return filter_by_control_period(period_pk=_control_period_pk, queryset=queryset)
        return queryset.iterator()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset(params=request.GET)
        total_count = Speakers.objects.count()

        context = {
            "object_list": queryset,
            "total_count": total_count,
            "control_periods": PeriodOfDiagnostics.objects.all()
        }
        return render(request, "devices/speakers/speakers_analytics_list.html", context)


class SpeakersAnalyticsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Speakers
    template_name = "devices/speakers/speakers_analytics_update.html"
    form_class = forms.SpeakersAnalyticsUpdateForm
    success_message = "Информация об обслуживании была успешно обновлена."
    success_url = reverse_lazy("headset_analytics_list")


class OutputDevicesInfoView(LoginRequiredMixin, TemplateView):
    template_name = "devices/output_info.html"


class OutputDevicesListView(LoginRequiredMixin, View):
    """Представление, выводящие все устройства вывода."""
    paginate_by = 4

    def get_queryset(self, params):
        _serial_number = params.get("serialNumber", "")


        printers = Printer.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model")
        monitors = Monitor.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model")
        headsets = Headset.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model")
        speakers = Speakers.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model")

        return {
            "printers": printers.iterator(),
            "monitors": monitors.iterator(),
            "headsets": headsets.iterator(),
            "speakers": speakers.iterator()
        }

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset(params=request.GET)
        total_count = Printer.objects.count() \
                      + Monitor.objects.count() \
                      + Headset.objects.count() \
                      + Speakers.objects.count()

        context = {
            **queryset,
            "total_count": total_count
        }
        return render(request, "devices/output/output_list.html", context)


class OutputDevicesAnalyticsListView(LoginRequiredMixin, View):
    def get_queryset(self, params):
        _serial_number = params.get("serialNumber", "")
        _control_period_pk = params.get("control_period")

        printers = Printer.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model") \
            .order_by("date_of_last_diagnostics")
        monitors = Monitor.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model") \
            .order_by("date_of_last_diagnostics")
        headsets = Headset.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model") \
            .order_by("date_of_last_diagnostics")
        speakers = Speakers.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model") \
            .order_by("date_of_last_diagnostics")

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
                "printers": filter(
                    lambda instance: filter_instance(instance),
                    printers.iterator()
                ),
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
            "printers": printers.iterator(),
            "monitors": monitors.iterator(),
            "headsets": headsets.iterator(),
            "speakers": speakers.iterator()
        }

    def get(self, request, *args, **kwargs):
        devices = self.get_queryset(params=request.GET)
        total_count = Printer.objects.count() \
                      + Monitor.objects.count() \
                      + Headset.objects.count() \
                      + Speakers.objects.count()

        context = {
            **devices,
            "total_count": total_count,
            "control_periods": PeriodOfDiagnostics.objects.all()
        }
        return render(request, "devices/output/output_analytics_list.html", context)
