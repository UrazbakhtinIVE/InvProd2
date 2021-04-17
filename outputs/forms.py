from django import forms

from mainapp.models import Category


class OutputsCategoriesForm(forms.Form):
	categories = forms.ModelChoiceField(
		queryset=Category.objects.all(),
		to_field_name="slug"
	)
	
	class Meta:
		widgets = {
            'categories': forms.Select(attrs={'class': 'form-control'}),
        }