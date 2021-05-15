from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)
from dal import autocomplete

from .forms import CartridgeCreateForm, CartridgeUpdateForm
from .models import Cartridge
from person.models import Person


class CartridgeInfo(LoginRequiredMixin, TemplateView):
    template_name = 'cartridges/cartridge_info.html'


class CartridgeListView(LoginRequiredMixin, ListView):
    model = Cartridge
    queryset = Cartridge.objects.all()
    context_object_name = 'cl'
    template_name = 'cartridges/cartridgeList.html'

    def get_queryset(self):
        query = self.request.GET.get('q', "")
        object_list = Cartridge.objects.filter(Q(serialNumber__contains=query))
        return object_list


class CartridgeDetailView(LoginRequiredMixin, DetailView):
    model = Cartridge
    queryset = Cartridge.objects.all()
    template_name = 'cartridges/cartridgeDetail.html'
    context_object_name = 'cd'


class CartridgeCreateView(LoginRequiredMixin, CreateView):
    model = Cartridge
    form_class = CartridgeCreateForm
    template_name = 'cartridges/cartridgeCreate.html'


class CartridgeUpdateView(LoginRequiredMixin, UpdateView):
    model = Cartridge
    form_class = CartridgeUpdateForm
    template_name = 'cartridges/cartridgeUpdate.html'
    context_object_name = 'cu'

class CartridgeDelete(LoginRequiredMixin, DeleteView):
    model = Cartridge
    template_name = 'cartridges/cartridgeDelete.html'
    context_object_name = 'cd'
    success_url = reverse_lazy('cartridge_list')


class SearchFirstNameAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    """API-представление, возращающее фамилию пользователя."""
    queryset = Person.objects.all()

    def get_queryset(self):
        queryset = self.queryset.filter(firstName__icontains=self.q)
        return queryset
