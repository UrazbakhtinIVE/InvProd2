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
    template_name = "schedulers/printers_scheduler_list.html"
    context_object_name = 'psl'

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        object_list = PrinterScheduler.objects.filter(device__serialNumber__contains=query)
        return object_list


class CartridgeSchedulerListView(LoginRequiredMixin, ListView):
    model = CartridgeScheduler
    template_name = 'schedulers/cartridges_scheduler_list.html'
    context_object_name = 'csl'

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        object_list = CartridgeScheduler.objects.filter(device__serialNumber__contains=query)
        return object_list


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