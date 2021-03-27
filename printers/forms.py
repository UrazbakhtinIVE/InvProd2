from django import forms

from dal import autocomplete

from printers.models import Printer, PrinterScheduler


# Атрибуты для кастомизации Select2 плагина для поля картриджей.
CARTRIDGE_ATTRS = {
    'data-placeholder': 'Выберите картридж',
    'data-allow-clear': "true",
    'cartridge-field': ""
}


class PrinterCreateForm(forms.ModelForm):

    class Meta:
        model = Printer
        fields = ('serialNumber','printerModel', 'status', 'name', 'ip',
                  'black_cartridge', 'blue_cartridge',
                  'yellow_cartridge', 'purple_cartridge')

        widgets = {
            'serialNumber':forms.TextInput(attrs={'class':'form-control'}),
            'printerModel': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'ip': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
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
        fields = ('status','location', 'black_cartridge',
                  'blue_cartridge', 'yellow_cartridge', 'purple_cartridge')
        widgets = {
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


class PrinterSchedulerCreateForm(forms.ModelForm):
    class Meta:
        model = PrinterScheduler
        fields = '__all__'

        widgets = {
            'uuid':forms.TextInput(attrs={'class': 'form-control'}),
            'printer':forms.Select(attrs={'class': 'form-control'}),
            'printerStatus': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PrinterSearchForm(forms.ModelForm):
    qwery = forms.CharField()
