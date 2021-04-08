from django import forms
from catriges.models import *
from dal import autocomplete

# Атрибуты для кастомизации Select2 плагина для поля картриджей.
PERSON_ATTRS = {
    'data-placeholder': 'Выберите картридж',
    'data-allow-clear': "true",
    'cartridge-field': ""
}


class CatrigeCreateForm(forms.ModelForm):
    class Meta:
        model = Catrige
        fields = '__all__'

        widgets = {
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'catrigeModel': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class CatrigeUpdateForm(forms.ModelForm):
    class Meta:
        model = Catrige
        fields = ('status', 'person', 'number')

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'person': autocomplete.ModelSelect2(
                url="search-first-name-autocomplete",
            )
        }
