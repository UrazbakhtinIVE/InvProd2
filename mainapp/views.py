from django.views.generic import *

class IndexView(TemplateView):
    template_name =  'mainapp/index.html'



class InfoView(TemplateView):
    template_name = 'mainapp/output_info.html'


class PrintView(TemplateView):
    template_name = 'printers/menuTemplate.html'



