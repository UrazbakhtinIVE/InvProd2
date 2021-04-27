from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'mainapp/index.html'


class InfoView(LoginRequiredMixin,TemplateView):
    template_name = 'mainapp/output_info.html'


class PrintView(LoginRequiredMixin,TemplateView):
    template_name = 'printers/menuTemplate.html'
