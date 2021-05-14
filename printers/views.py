from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    View, TemplateView, DetailView, ListView, CreateView, UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from dal import autocomplete

from cartridges.models import Cartridge
from printers.utils import PrinterAnalyticsResource
from .forms import PrinterCreateForm, PrinterUpdateForm, PrinterAnalyzUpdateForm
from .models import Printer


class PrinterInfo(LoginRequiredMixin, TemplateView):
    template_name = 'printers/printer_info.html'


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


class PrinterListView(LoginRequiredMixin, ListView):
    model = Printer
    template_name = 'printers/printerList.html'
    context_object_name = 'pl'

    def get_queryset(self):
        query = self.request.GET.get('q', "")
        object_list = Printer.objects.filter(Q(serialNumber__contains=query))
        return object_list


class PrinterDetailView(LoginRequiredMixin, DetailView):
    model = Printer
    queryset = Printer.objects.all()
    template_name = 'printers/printerDetail.html'
    context_object_name = 'pd'


class PrinterCreateView(SuccessMessageMixin, CreateView):
    model = Printer
    form_class = PrinterCreateForm
    template_name = 'printers/printerCreate.html'
    context_object_name = 'pc'

    def get_success_message(self, cleaned_data):
        return "Новый принтер был успешно создан."


class PrinterUpdateView(SuccessMessageMixin, UpdateView):
    model = Printer
    template_name = 'printers/printerUpdate.html'
    form_class = PrinterUpdateForm
    context_object_name = 'pu'
    success_message = "Информация о принтере была успешно обновлена."


class PrinterAnalyzUpdateView(SuccessMessageMixin, UpdateView):
    model = Printer
    template_name = 'printers/printAnalyzUpdate.html'
    form_class = PrinterAnalyzUpdateForm
    context_object_name = 'pau'
    success_url = reverse_lazy("diagnostics_list")


class PrinterAnalyticsListView(LoginRequiredMixin, ListView):
    model = Printer
    template_name = 'printers/printerAnalyticsList.html'
    context_object_name = 'pl'


class PrinterAnalytics(LoginRequiredMixin, TemplateView):
    template_name = 'printers/printerAnalytics.html'


class ExportPrintersAnalytics(View):

    def get(self, *args, **kwargs):
        import datetime
        now = datetime.datetime.now()
        dataset = PrinterAnalyticsResource().export()
        response = HttpResponse(
            dataset.xlsx, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response['Content-Disposition'] = f'attachment; filename=PrintersAnalytics ({now}).xlsx'
        return response
