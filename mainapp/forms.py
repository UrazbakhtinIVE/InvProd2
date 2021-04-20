from django import forms
from durationwidget.widgets import TimeDurationWidget
from .models import PeriodOfDiagnostics



class DurationFieldFormMixin(forms.ModelForm):
    
    period = forms.DurationField(
        label="Период диагностики",
        widget=TimeDurationWidget(show_days=True, show_hours=False, show_minutes=False, show_seconds=False), required=False
    )


class AdminPeriodOfDiagnosticsForm(DurationFieldFormMixin):

    class Meta:
        model = PeriodOfDiagnostics
        fields = "__all__"