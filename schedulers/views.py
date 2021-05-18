import itertools

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, View

from .models import (
    PrinterScheduler, CartridgeScheduler, MonitorScheduler,
    HeadsetScheduler, SpeakersScheduler
)


class PrinterSchedulerListView(LoginRequiredMixin, ListView):
    model = PrinterScheduler
    template_name = "schedulers/printer_scheduler_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        _serial_number = self.request.GET.get("serialNumber", "")
        return queryset \
            .filter(device__serialNumber__icontains=_serial_number) \
            .select_related("device")


class CartridgeSchedulerListView(LoginRequiredMixin, ListView):
    model = CartridgeScheduler
    template_name = 'schedulers/cartridge_scheduler_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        _serial_number = self.request.GET.get("serialNumber", "")
        return queryset \
            .filter(device__serialNumber__icontains=_serial_number) \
            .select_related("device")


class MonitorSchedulerListView(LoginRequiredMixin, ListView):
    model = MonitorScheduler
    template_name = "schedulers/monitor_scheduler_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        _serial_number = self.request.GET.get("serialNumber", "")
        return queryset \
            .filter(device__serialNumber__icontains=_serial_number) \
            .select_related("device")

class HeadsetSchedulerListView(LoginRequiredMixin, ListView):
    model = HeadsetScheduler
    template_name = "schedulers/headset_scheduler_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        _serial_number = self.request.GET.get("serialNumber", "")
        return queryset \
            .filter(device__serialNumber__icontains=_serial_number) \
            .select_related("device")

class SpeakersSchedulerListView(LoginRequiredMixin, ListView):
    model = SpeakersScheduler
    template_name = "schedulers/speakers_scheduler_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        _serial_number = self.request.GET.get("serialNumber", "")
        return queryset \
            .filter(device__serialNumber__icontains=_serial_number) \
            .select_related("device")

class DevicesSchedulerListView(View):

    def get_queryset(self, params):
        _serial_number = params.get("serialNumber", "")

        monitors_scheduler = MonitorScheduler.objects \
            .filter(device__serialNumber__icontains=_serial_number) \
            .select_related("device")
        headsets_scheduler = HeadsetScheduler.objects \
            .filter(device__serialNumber__icontains=_serial_number) \
            .select_related("device")
        speakers_scheduler = SpeakersScheduler.objects \
            .filter(device__serialNumber__icontains=_serial_number)\
            .select_related("device")


        return itertools.chain(monitors_scheduler, headsets_scheduler, speakers_scheduler)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset(request.GET)

        context = {"dsl": queryset}
        return render(request, 'schedulers/devices_scheduler_list.html', context)