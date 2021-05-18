import datetime

from mainapp.models import PeriodOfDiagnostics


def filter_by_control_period(queryset, period_pk):
    control_period = PeriodOfDiagnostics.objects.get(pk=period_pk)
    now = datetime.date.today()

    def filter_instance(instance):
        """период диагностики + дата последней диагностики
            < текущая дата + контрольный период диагностики
        """
        if not instance.period_of_product_diagnostics:
            return
        if (instance.period_of_product_diagnostics.period
                + instance.date_of_last_diagnostics
                < now + control_period.period):
            return instance

    return filter(
        lambda instance: filter_instance(instance),
        queryset.iterator()
    )