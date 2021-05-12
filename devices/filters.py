import django_filters

from .models import Monitor, Speakers, Headset
from mainapp.models import PeriodOfDiagnostics


class DevicesFilterSet(django_filters.FilterSet):
    serialNumber = django_filters.CharFilter(lookup_expr='icontains')

    control_period = django_filters.ModelChoiceFilter(
        queryset=PeriodOfDiagnostics.objects.order_by('period'),
        empty_label='Контрольные периоды')