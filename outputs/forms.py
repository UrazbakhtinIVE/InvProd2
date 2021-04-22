from dal import autocomplete
from django import forms
from mainapp.models import Category
from outputs.models import Monitor


class OutputsCategoriesForm(forms.Form):
    categories = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        to_field_name="slug", widget=forms.Select(attrs={'class': 'form-control'})
    )


class MonitorCreateForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ('model', 'serialNumber',)

        widgets = {
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
        }


class MonitorUpdateForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ('status', 'person')

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'person': autocomplete.ModelSelect2(
                url="search-first-name-autocomplete",
            )
        }
