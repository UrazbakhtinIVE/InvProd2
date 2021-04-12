from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import *
from catriges.forms import *
from dal import autocomplete


class CatrigeInfo(TemplateView):
    template_name = 'catrige/catrige_info.html'



class CatrigeListView(ListView):
    model = Catrige
    queryset = Catrige.objects.all()
    context_object_name = 'cl'
    template_name = 'catrige/catrigeList.html'

    def get_queryset(self):
        query = self.request.GET.get('q', "")
        object_list = Catrige.objects.filter(Q(serialNumber__contains=query))
        return object_list


class CatrigeDetailView(DetailView):
    model = Catrige
    queryset = Catrige.objects.all()
    template_name = 'catrige/catrigeDetail.html'
    context_object_name = 'cd'


class CatrigeCreateView(CreateView):
    model = Catrige
    queryset = Catrige.objects.filter(status=CatrigeScheduler.catrigeStatus)
    form_class = CatrigeCreateForm
    template_name = 'catrige/catrigeCreate.html'


class CatrigeUpdateView(UpdateView):
    model = Catrige
    form_class = CatrigeUpdateForm
    template_name = 'catrige/catrigeUpdate.html'
    context_object_name = 'cu'

class CatrigeDelete(DeleteView):
    model = Catrige
    template_name = 'catrige/catrigeDelete.html'
    context_object_name = 'cd'
    success_url = reverse_lazy('catrige_list')


class CatrigeSchedulerListView(ListView):
    model = CatrigeScheduler
    queryset = CatrigeScheduler.objects.all()
    template_name = 'catrige/catrigeSchedulerList.html'
    context_object_name = 'csl'

    def get_queryset(self):
        query = self.request.GET.get('q', "")
        object_list = CatrigeScheduler.objects.filter(Q(catrige__serialNumber__contains=query))
        return object_list


class SearchFirstNameAutocomplete(autocomplete.Select2QuerySetView):
    """API-представление, возращающее фамилию пользователя."""
    queryset = Person.objects.all()

    def get_queryset(self):
        queryset = self.queryset.filter(firstName__icontains=self.q)
        return queryset
