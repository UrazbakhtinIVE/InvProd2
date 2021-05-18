from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
)
from dal import autocomplete

from . import forms
from .models import Cartridge
from person.models import Person
from mainapp.models import PeriodOfDiagnostics
from mainapp.utils import filter_by_control_period


class CartridgeInfoView(LoginRequiredMixin, TemplateView):
    template_name = "cartridges/cartridge_info.html"

class CartridgeListView(LoginRequiredMixin, ListView):
    model = Cartridge
    template_name = "cartridges/cartridge_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        _serial_number = self.request.GET.get("serialNumber", "")
        return queryset \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model")

class CartridgeDetailView(LoginRequiredMixin, DetailView):
    model = Cartridge
    template_name = "cartridges/cartridge_detail.html"
    context_object_name = "cd"

class CartridgeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cartridge
    form_class = forms.CartridgeCreateForm
    success_message = "Новый картридж был успешно создан."
    template_name = "cartridges/cartridge_сreate.html"

class CartridgeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cartridge
    form_class = forms.CartridgeUpdateForm
    success_message = "Информация о картридже была успешно обновлена."
    template_name = "cartridges/cartridge_update.html"

class CartridgeDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Cartridge
    template_name = "cartridges/cartridge_delete.html"
    success_message = "Картридж был успешно удален."
    success_url = reverse_lazy("cartridge_list")

class CartridgeAnalyticsListView(LoginRequiredMixin, View):
    def get_queryset(self, params):
        _serial_number = params.get("serialNumber", "")
        _control_period_pk = params.get("control_period")

        queryset = Cartridge.objects \
            .filter(serialNumber__icontains=_serial_number) \
            .select_related("model") \
            .order_by("date_of_last_diagnostics")

        if _control_period_pk:
            return filter_by_control_period(period_pk=_control_period_pk, queryset=queryset)
        return queryset.iterator()


    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset(params=request.GET)
        total_count = Cartridge.objects.count()

        context = {
            "object_list": queryset,
            "total_count": total_count,
            "control_periods": PeriodOfDiagnostics.objects.all()
        }
        return render(request, "cartridges/cartridge_analytics_list.html", context)

class CartridgeAnalyticsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cartridge
    template_name = "cartridges/cartridge_analytics_update.html"
    form_class = forms.CartridgeAnalyticsUpdateForm
    success_message = "Информация об обслуживании была успешно обновлена."
    success_url = reverse_lazy("cartridge_analytics_list")


class SearchFirstNameAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    """API-представление, возращающее фамилию пользователя."""
    queryset = Person.objects.all()

    def get_queryset(self):
        queryset = self.queryset.filter(firstName__icontains=self.q)
        return queryset
