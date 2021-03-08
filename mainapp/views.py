from django.views.generic import *

class IndexView(TemplateView):
    template_name =  'mainapp/index.html'



class PrinterTemplate(TemplateView):
    template_name = 'mainapp/menuTemplate.html'

