from django import forms

from mainapp.models import Category
from outputs.models import Monitor


class OutputsCategoriesForm(forms.Form):
    categories = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        to_field_name="slug"
    )

    class Meta:
        widgets = {
            'categories': forms.Select(attrs={'class': 'form-control'}),
        }


class MonitorCreateForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = '__all__'

        widgets = {
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
        }
