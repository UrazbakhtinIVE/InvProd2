from django import forms
from catriges.models import *


class CatrigeCreateForm(forms.ModelForm):

    class Meta:
        model = Catrige
        fields = '__all__'

        widgets = {
            'serialNumber':forms.TextInput(attrs={'class':'form-control'}),
            'catrigeModel': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }
