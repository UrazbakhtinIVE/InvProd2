from dal import autocomplete
from django import forms
from mainapp.models import Category, PeriodOfDiagnostics
from devices.models import Monitor, Headset


class DevicesCategoriesForm(forms.Form):
    categories = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        to_field_name="slug", widget=forms.Select(attrs={'class': 'form-control'})
    )

class MonitorCreateForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ('model', 'serialNumber', 'status')

        widgets = {
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class MonitorUpdateForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ('status', 'person', 'location', 'description')

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),

            'person': autocomplete.ModelSelect2(
                url="search-first-name-autocomplete",
            )

        }


class HeadsetForm(forms.ModelForm):
    class Meta:
        model = Headset
        fields = ('model', 'serialNumber')

        widgets = {
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
