from django.db.models import Q
from django.views.generic import *
from printers.forms import *
from printers.models import *



class PrinterListView(ListView):
    model = Printer
    template_name = 'printers/printerList.html'
    context_object_name = 'pl'

    def get_queryset(self):
        query = self.request.GET.get('q', "")
        object_list = Printer.objects.filter(Q(serialNumber__contains=query))
        return object_list




class PrinterDetailView(DetailView):
    model = Printer
    queryset = Printer.objects.all()
    template_name = 'printers/printerDetail.html'
    context_object_name = 'pd'


class PrinterCreateView(CreateView):
    model = Printer
    queryset = Printer.objects.filter(status__name=PrinterScheduler.printerStatus)
    form_class = PrinterCreateForm
    template_name = 'printers/printerCreate.html'
    context_object_name = 'pc'



class PrinterUpdateView(UpdateView):
    model = Printer
    template_name = 'printers/printerUpdate.html'
    form_class = PrinterUpdateForm
    context_object_name = 'pu'



class PrinterSchedulerListView(ListView):
    model = PrinterScheduler
    queryset = PrinterScheduler.objects.all()
    template_name = 'printers/printerSchedulerList.html'
    context_object_name = 'psl'

    def get_queryset(self):
        query = self.request.GET.get('q', "")
        object_list = PrinterScheduler.objects.filter(Q(printer__serialNumber__contains= query))
        return object_list


class PrinterShedulerCreateView(CreateView):
    model = PrinterScheduler
    form_class = PrinterSchedulerCreateForm
    template_name = 'printers/create_printer_scheduler.html'
    context_object_name = 'cp'







