from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import View, TemplateView

from .devices_analytics import (
    PrinterAnalyticsResource, CartridgeAnalyticsResource, OutputDevicesAnalyticsResource
)

class Wellcome(TemplateView):
   template_name = 'mainapp/wellcome.html'

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'mainapp/index.html'


class InfoView(LoginRequiredMixin, TemplateView):
    template_name = 'mainapp/devices_info.html'


class OutputsDevicesInfoView(LoginRequiredMixin, TemplateView):
    template_name = "mainapp/devices_outputs.html"


class InputsDevicesInfoView(LoginRequiredMixin, TemplateView):
    template_name = "mainapp/devices_inputs.html"


class OthersDevicesInfoView(LoginRequiredMixin, TemplateView):
    template_name = "mainapp/devices_others.html"


class PrintView(LoginRequiredMixin,TemplateView):
    template_name = 'printers/menuTemplate.html'


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


class ExportCartridgeAnalytics(View):

    def get(self, *args, **kwargs):
        import datetime
        now = datetime.datetime.now()
        dataset = CartridgeAnalyticsResource().export()
        response = HttpResponse(
            dataset.xlsx, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response['Content-Disposition'] = f'attachment; filename=CartridgeAnalytics ({now}).xlsx'
        return response


class ExportOutputDevicesAnalytics(View):

    def get(self, *args, **kwargs):
        import datetime
        now = datetime.datetime.now()
        dataset = OutputDevicesAnalyticsResource().export()
        response = HttpResponse(
            dataset.xlsx, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response['Content-Disposition'] = f'attachment; filename=DevicesAnalytics ({now}).xlsx'
        return response