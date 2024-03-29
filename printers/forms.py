from django import forms
from dal import autocomplete
from printers.models import Printer

from mainapp.forms import DurationFieldFormMixin


# Атрибуты для кастомизации Select2 плагина для поля картриджей.
CARTRIDGE_ATTRS = {
    'data-placeholder': 'Выберите картридж',
    'data-allow-clear': "true",
    'cartridges-field': ""
}


class PrinterCreateForm(forms.ModelForm):

    class Meta:
        model = Printer
        fields = ('serialNumber', 'model', 'status', 'name', 'ip', 'location',
                  'black_cartridge', 'blue_cartridge',
                  'yellow_cartridge', 'purple_cartridge')

        widgets = {
            'serialNumber':forms.TextInput(attrs={'class':'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'ip': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'black_cartridge': autocomplete.ModelSelect2(
                url="black-cartridges-autocomplete",
                attrs=CARTRIDGE_ATTRS
            ),
            'blue_cartridge': autocomplete.ModelSelect2(
                url="blue-cartridges-autocomplete",
                attrs=CARTRIDGE_ATTRS
            ),
            'yellow_cartridge': autocomplete.ModelSelect2(
                url="yellow-cartridges-autocomplete",
                attrs=CARTRIDGE_ATTRS
            ),
            'purple_cartridge': autocomplete.ModelSelect2(
                url="purple-cartridges-autocomplete",
                attrs=CARTRIDGE_ATTRS
            ),
        }


class PrinterUpdateForm(forms.ModelForm):

    class Meta:
        model = Printer
        fields = ('status', 'black_cartridge','location', 'description',
                  'blue_cartridge', 'yellow_cartridge', 'purple_cartridge')
        widgets = {
            'description' :forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'black_cartridge': autocomplete.ModelSelect2(
                url="black-cartridges-autocomplete",
                attrs=CARTRIDGE_ATTRS
            ),
            'blue_cartridge': autocomplete.ModelSelect2(
                url="blue-cartridges-autocomplete",
                attrs=CARTRIDGE_ATTRS
            ),
            'yellow_cartridge': autocomplete.ModelSelect2(
                url="yellow-cartridges-autocomplete",
                attrs=CARTRIDGE_ATTRS
            ),
            'purple_cartridge': autocomplete.ModelSelect2(
                url="purple-cartridges-autocomplete",
                attrs=CARTRIDGE_ATTRS
            ),
        }


class PrinterAnalyzUpdateForm(forms.ModelForm):

    class Meta:
        model = Printer
        fields = ('date_of_last_diagnostics', 'period_of_product_diagnostics', 'description')

        widgets = {
            'date_of_last_diagnostics': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'period_of_product_diagnostics':forms.Select(attrs={'class': 'form-control'}),
        }


class PrinterSearchForm(forms.ModelForm):
    qwery = forms.CharField()


class PrinterAdminForm(DurationFieldFormMixin):

    class Meta:
        model = Printer
        fields = "__all__"