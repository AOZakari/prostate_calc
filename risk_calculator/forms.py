from django import forms
from .models import Person_Input
class Prediction(forms.ModelForm):
    class Meta:
        model = Person_Input
        fields = ['age', 'brothers', 'sisters', 'older_brothers', 'older_sisters', 'dark_skin', 'past_cancer', 'past_breast_cancer', 'past_other_cancer', 'father_prostate', 'mother_breast', 'brother_prostate', 'sister_prostate', 'mutation', 'psa', 'volume_prostate', 'weight', 'height', 'low_testosterone', 'sexual_difficulties', 'heat', 'medicine_fin_dist', 'medicine_erection', 'medicine_cholesterol']
        widgets = {
            'age': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'brothers': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'sisters': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'older_brothers': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'older_sisters': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'dark_skin': forms.CheckboxInput(
				attrs={
					'class': 'form-control'
					}
				),
            'past_cancer': forms.CheckboxInput(
				attrs={
					'class': 'form-control'
					}
				),
            'medicine_cholesterol': forms.CheckboxInput(
				attrs={
					'class': 'form-control'
					}
				),
            'medicine_erection': forms.CheckboxInput(
				attrs={
					'class': 'form-control'
					}
				),
            'past_breast_cancer': forms.CheckboxInput(
				attrs={
					'class': 'form-control'
					}
				),
            'past_other_cancer': forms.CheckboxInput(
				attrs={
					'class': 'form-control'
					}
				),
            'father_prostate': forms.CheckboxInput(
				attrs={
					'class': 'form-control'
					}
				),
            'mother_breast': forms.CheckboxInput(
				attrs={
					'class': 'form-control'
					}
				),
            'brother_prostate': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'sister_prostate': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'mutation': forms.CheckboxInput(
				attrs={
					'class': 'form-control'
					}
				),
            'psa': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'volume_prostate': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'weight': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'height': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'low_testosterone': forms.CheckboxInput(
				attrs={
					'class': 'form-control'
					}
				),
            'sexual_difficulties': forms.CheckboxInput(
				attrs={
					'class': 'form-control'
					}
				),
            'heat': forms.CheckboxInput(
				attrs={
					'class': 'form-control'
					}
				),
            'medicine_fin_dist': forms.CheckboxInput(
				attrs={
					'class': 'form-control'
					}
				),
            }