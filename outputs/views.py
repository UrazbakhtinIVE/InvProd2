from itertools import chain
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, FormView, CreateView
from django.urls import reverse_lazy
from outputs.models import Monitor, Headset, Speakers
from mainapp.models import Category
from .forms import OutputsCategoriesForm


class OutputsView(TemplateView):
    template_name = 'outputs/outputs_info.html'


class OutputsListView(LoginRequiredMixin, TemplateView):
    """Представление, выводящие все устройства."""

    monitors = Monitor.objects.all()
    headsets = Headset.objects.all()
    speakers = Speakers.objects.all()
    template_name = 'outputs/outputsList.html'
    extra_context = {
        "monitors": monitors,
        "headsets": headsets,
        "speakers": speakers
    }


class AddOutputFromCategory(FormView):
    template_name = 'outputs/outputsCreateTemplate.html'
    form_class = OutputsCategoriesForm


class AddMonitorView(CreateView):

    model = Monitor
    template_name = "outputs/createMonitor.html"
    fields = "__all__"
    success_url = reverse_lazy("output_list")


class AddHeadsetView(CreateView):

    model = Headset
    template_name = "outputs/createHeadset.html"
    fields = "__all__"
    success_url = reverse_lazy("output_list")


class AddSpeakerView(CreateView):

    model = Speakers
    template_name = "outputs/createSpeaker.html"
    fields = "__all__"
    success_url = reverse_lazy("output_list")
