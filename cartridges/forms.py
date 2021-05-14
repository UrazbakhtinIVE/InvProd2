from django import forms
from dal import autocomplete

from cartridges.models import Cartridge


# Атрибуты для кастомизации Select2 плагина для поля картриджей.
PERSON_ATTRS = {
    'data-placeholder': 'Выберите картридж',
    'data-allow-clear': "true",
    'cartridges-field': ""
}


class CartridgeCreateForm(forms.ModelForm):
    class Meta:
        model = Cartridge
        fields = '__all__'

        widgets = {
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'cartridgeModel': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class CartridgeUpdateForm(forms.ModelForm):
    class Meta:
        model = Cartridge
        fields = ('status', 'person', 'description')

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),

            'person': autocomplete.ModelSelect2(
                url="search-first-name-autocomplete",
            )
        }
