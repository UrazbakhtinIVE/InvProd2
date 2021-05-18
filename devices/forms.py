from django import forms
from dal import autocomplete

from mainapp.models import Category, PeriodOfDiagnostics
from devices.models import Monitor, Headset, Speakers


class DevicesCategoriesForm(forms.Form):
    categories = forms.ChoiceField(
        choices=(
            (None, "-----"),
            ("monitors", "Мониторы"),
            ("headsets", "Гарнитуры"),
            ("speakers", "Колонки"),
            ("printers", "Принтеры"),
            ("cartridges", "Картриджи")
        ),
        widget=forms.Select(attrs={"class": "form-control"})
    )


class MonitorCreateForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ("model", "serialNumber", "status")

        widgets = {
            "serialNumber": forms.TextInput(attrs={"class": "form-control"}),
            "model": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }

class MonitorUpdateForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ("status", "person", "location", "description")

        widgets = {
            "status": forms.Select(attrs={"class": "form-control"}),
            "location": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),

            "person": autocomplete.ModelSelect2(url="search-first-name-autocomplete")
        }

class MonitorAnalyticsUpdateForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ("date_of_last_diagnostics", "period_of_product_diagnostics")

        widgets = {
            "date_of_last_diagnostics": forms.SelectDateWidget(attrs={"class": "form-control"}),
            "period_of_product_diagnostics": forms.Select(attrs={"class": "form-control"}),
        }


class HeadsetCreateForm(forms.ModelForm):
    class Meta:
        model = Headset
        fields = ("model", "serialNumber", "status")

        widgets = {
            "serialNumber": forms.TextInput(attrs={"class": "form-control"}),
            "model": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }

class HeadsetUpdateForm(forms.ModelForm):
    class Meta:
        model = Headset
        fields = ("status", "person", "location", "description")

        widgets = {
            "status": forms.Select(attrs={"class": "form-control"}),
            "location": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),

            "person": autocomplete.ModelSelect2(url="search-first-name-autocomplete")
        }

class HeadsetAnalyticsUpdateForm(forms.ModelForm):
    class Meta:
        model = Headset
        fields = ("date_of_last_diagnostics", "period_of_product_diagnostics")

        widgets = {
            "date_of_last_diagnostics": forms.SelectDateWidget(attrs={"class": "form-control"}),
            "period_of_product_diagnostics": forms.Select(attrs={"class": "form-control"}),
        }


class SpeakersCreateForm(forms.ModelForm):
    class Meta:
        model = Speakers
        fields = ("model", "serialNumber", "status")

        widgets = {
            "serialNumber": forms.TextInput(attrs={"class": "form-control"}),
            "model": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }


class SpeakersUpdateForm(forms.ModelForm):
    class Meta:
        model = Speakers
        fields = ("status", "person", "location", "description")

        widgets = {
            "status": forms.Select(attrs={"class": "form-control"}),
            "location": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),

            "person": autocomplete.ModelSelect2(url="search-first-name-autocomplete")
        }

class SpeakersAnalyticsUpdateForm(forms.ModelForm):
    class Meta:
        model = Speakers
        fields = ("date_of_last_diagnostics", "period_of_product_diagnostics")

        widgets = {
            "date_of_last_diagnostics": forms.SelectDateWidget(attrs={"class": "form-control"}),
            "period_of_product_diagnostics": forms.Select(attrs={"class": "form-control"}),
        }