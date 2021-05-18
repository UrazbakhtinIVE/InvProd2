from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from dal import autocomplete

from cartridges.models import Cartridge
from mainapp.models import PeriodOfDiagnostics
from mainapp.utils import filter_by_control_period
from .forms import PrinterCreateForm, PrinterUpdateForm, PrinterAnalyzUpdateForm
from .models import Printer


class BlackCartridgesAutocomplete(autocomplete.Select2QuerySetView):
    """API-представление, возращающее черные картриджи по запросу."""
    queryset = Cartridge.objects.get_black_cartridges()

    def get_queryset(self):
        queryset = self.queryset.filter(
            Q(black_cartridge=None)
            & ~Q(status="onrefill")
            & Q(serialNumber__icontains=self.q)
        )
        return queryset

class BlueCartridgesAutocomplete(autocomplete.Select2QuerySetView):
    """API-представление, возращающее голубые картриджи по запросу."""
    queryset = Cartridge.objects.get_blue_cartridges()

    def get_queryset(self):
        queryset = self.queryset.filter(
            Q(blue_cartridge=None)
            & ~Q(status="onrefill")
            & Q(serialNumber__icontains=self.q)
        )
        return queryset

class YellowCartridgesAutocomplete(autocomplete.Select2QuerySetView):
    """API-представление, возращающее желтые картриджи по запросу."""
    queryset = Cartridge.objects.get_yellow_cartridges()

    def get_queryset(self):
        queryset = self.queryset.filter(
            Q(yellow_cartridge=None)
            & ~Q(status="onrefill")
            & Q(serialNumber__icontains=self.q)
        )
        return queryset

class PurpleCartridgesAutocomplete(autocomplete.Select2QuerySetView):
    """API-представление, возращающее пурпурные картриджи по запросу."""
    queryset = Cartridge.objects.get_purple_cartridges()

    def get_queryset(self):
        queryset = self.queryset.filter(
            Q(purple_cartridge=None)
            & ~Q(status="onrefill")
            & Q(serialNumber__icontains=self.q)
        )
        return queryset


class PrinterInfoView(LoginRequiredMixin, TemplateView):
    template_name = "printers/printer_info.html"

class PrinterListView(LoginRequiredMixin, ListView):
    model = Printer
    extra_context = {"total_count": Printer.objects.count()}
    template_name = "printers/printer_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        _serial_number = self.request.GET.get("serialNumber", "")
        return queryset \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model")

class PrinterDetailView(LoginRequiredMixin, DetailView):
    model = Printer
    template_name = "printers/printer_detail.html"

class PrinterCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Printer
    form_class = PrinterCreateForm
    template_name = "printers/printer_create.html"
    success_message = "Новый принтер был успешно создан."
    success_url = reverse_lazy("printer_list")

class PrinterUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Printer
    template_name = "printers/printer_update.html"
    form_class = PrinterUpdateForm
    success_message = "Информация о принтере была успешно обновлена."
    success_url = reverse_lazy("printer_list")

class PrinterDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Printer
    template_name = "printers/printer_delete.html"
    success_message = "Принтер был успешно удален."
    success_url = reverse_lazy("printer_list")

class PrinterAnalyticsListView(LoginRequiredMixin, ListView):
    def get_queryset(self, params):
        _serial_number = params.get("serialNumber", "")
        _control_period_pk = params.get("control_period")

        queryset = Printer.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model") \
            .order_by("date_of_last_diagnostics")

        if _control_period_pk:
            return filter_by_control_period(period_pk=_control_period_pk, queryset=queryset)
        return queryset.iterator()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset(params=request.GET)
        total_count = Printer.objects.count()

        context = {
            "object_list": queryset,
            "total_count": total_count,
            "control_periods": PeriodOfDiagnostics.objects.all()
        }
        return render(request, "printers/printer_analytics_list.html", context)

class PrinterAnalyticsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Printer
    template_name = "printers/printer_analytics_update.html"
    form_class = PrinterAnalyzUpdateForm
    success_message = "Информация об обслуживании была успешно обновлена."
    success_url = reverse_lazy("printer_analytics_list")
