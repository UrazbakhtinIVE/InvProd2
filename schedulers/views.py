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
        object_list = PrinterScheduler.objects.filter(printer__serialNumber__contains=query)
        return object_list


class CartridgeSchedulerListView(LoginRequiredMixin, ListView):
    model = CartridgeScheduler
    template_name = 'schedulers/cartridges_scheduler_list.html'
    context_object_name = 'csl'

    def get_queryset(self):
        query = self.request.GET.get('q', "")
        object_list = CartridgeScheduler.objects.filter(cartridge__serialNumber__contains=query)
        return object_list


class DevicesSchedulerListView(View):

    def get(self, request, *args, **kwargs):
        monitors = MonitorScheduler.objects.all()
        headsets = HeadsetScheduler.objects.all()
        speakers = SpeakersScheduler.objects.all()

        context = {"dsl": itertools.chain(monitors, headsets, speakers)}
        return render(request, 'schedulers/devices_scheduler_list.html', context)