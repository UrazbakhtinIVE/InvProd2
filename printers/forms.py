from django import forms
from printers.models import Printer, PrinterScheduler


class PrinterCreateForm(forms.ModelForm):

    class Meta:
        model = Printer
        fields = ('serialNumber','printerModel', 'status', 'name', 'ip')

        widgets = {
            'serialNumber':forms.TextInput(attrs={'class':'form-control'}),
            'printerModel': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'ip': forms.TextInput(attrs={'class':'form-control'}),
        }



class PrinterUpdateForm(forms.ModelForm):

    class Meta:
        model = Printer
        fields = ('status','location')

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
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
