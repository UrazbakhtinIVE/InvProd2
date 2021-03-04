from django.views.generic import *
from printers.forms import *
from printers.models import *


class PrinterTemplate(TemplateView):
    template_name = 'printers/printerTemplate.html'


class PrinterList(ListView):
    model = Printer
    queryset = Printer.objects.all()
    template_name = 'printers/printerList.html'
    context_object_name = 'pl'


class PrinterDetail(DetailView):
    model = Printer
    queryset = Printer.objects.all()
    template_name = 'printers/printerDetail.html'
    context_object_name = 'pd'


class PrinterCreate(CreateView):
    model = Printer
    queryset = Printer.objects.filter(status__name=PrinterScheduler.printerStatus)
    form_class = PrinterCreateForm
    template_name = 'printers/printerCreate.html'
    context_object_name = 'pc'



class PrinterUpdate(UpdateView):
    model = Printer
    template_name = 'printers/printerUpdate.html'
    form_class = PrinterUpdateForm
    context_object_name = 'pu'




class PrinterSchedulerList(ListView):
    model = PrinterScheduler
    queryset = PrinterScheduler.objects.all()
    template_name = 'printers/printerSchedulerList.html'
    context_object_name = 'psl'




class PrinterShedulerCreate(CreateView):
    model = PrinterScheduler
    form_class = PrinterSchedulerCreateForm
    template_name = 'printers/create_printer_scheduler.html'
    context_object_name = 'cp'








