from django.db.models import Q
from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from printers.forms import *
from printers.models import *
from catriges.models import Catrige


class PrinterInfo(LoginRequiredMixin, TemplateView):
    template_name = 'printers/printer_info.html'


class BlackCartridgesAutocomplete(autocomplete.Select2QuerySetView):
    """API-представление, возращающее черные картриджи по запросу."""
    queryset = Catrige.objects.get_black_cartridges()

    def get_queryset(self):
        queryset = self.queryset.filter(
            Q(black_cartridge=None)
            & ~Q(status="onrefill")
            & Q(serialNumber__icontains=self.q)
        )
        return queryset


class BlueCartridgesAutocomplete(autocomplete.Select2QuerySetView):
    """API-представление, возращающее голубые картриджи по запросу."""
    queryset = Catrige.objects.get_blue_cartridges()

    def get_queryset(self):
        queryset = self.queryset.filter(
            Q(blue_cartridge=None)
            & ~Q(status="onrefill")
            & Q(serialNumber__icontains=self.q)
        )
        return queryset


class YellowCartridgesAutocomplete(autocomplete.Select2QuerySetView):
    """API-представление, возращающее желтые картриджи по запросу."""
    queryset = Catrige.objects.get_yellow_cartridges()

    def get_queryset(self):
        queryset = self.queryset.filter(
            Q(yellow_cartridge=None)
            & ~Q(status="onrefill")
            & Q(serialNumber__icontains=self.q)
        )
        return queryset


class PurpleCartridgesAutocomplete(autocomplete.Select2QuerySetView):
    """API-представление, возращающее пурпурные картриджи по запросу."""
    queryset = Catrige.objects.get_purple_cartridges()

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
    queryset = Printer.objects.filter(status__name=PrinterScheduler.printerStatus)
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


class PrinterSchedulerListView(LoginRequiredMixin, ListView):
    model = PrinterScheduler
    queryset = PrinterScheduler.objects.all()
    template_name = 'printers/printerSchedulerList.html'
    context_object_name = 'psl'

    def get_queryset(self):
        query = self.request.GET.get('q', "")
        object_list = PrinterScheduler.objects.filter(Q(printer__serialNumber__contains=query))
        return object_list


class PrinterShedulerCreateView(LoginRequiredMixin, CreateView):
    model = PrinterScheduler
    form_class = PrinterSchedulerCreateForm
    template_name = 'printers/create_printer_scheduler.html'
    context_object_name = 'cp'


class PrinterAnalyticsListView(LoginRequiredMixin, ListView):
    model = Printer
    template_name = 'printers/printerAnalyticsList.html'
    context_object_name = 'pl'
