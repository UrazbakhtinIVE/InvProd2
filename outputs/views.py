from itertools import chain
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from outputs.models import Monitor, Headset, Speakers
from mainapp.models import Category


class OutputsView(TemplateView):
    template_name = 'outputs/outputs_info.html'


class OutputsListView(LoginRequiredMixin, ListView):
    """Представление, выводящие все устройства."""

    monitors = Monitor.objects.all()
    headsets = Headset.objects.all()
    speakers = Speakers.objects.all()
    template_name = 'outputs/outputsList.html'

    def get_queryset(self):
        return chain(self.monitors, self.headsets, self.speakers)


class SelectCategoryView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'outputs/outputsCreateTemplate.html'
    context_object_name = 'category'


