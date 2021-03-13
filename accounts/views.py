from django.shortcuts import render
from django.views.generic import TemplateView


class Wellcome(TemplateView):
   template_name = 'accounts/wellcome.html'