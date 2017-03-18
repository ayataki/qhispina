from django import forms

from .models import Pet


class PetForm (forms.ModelForm):

    class Meta:
        model = Pet

        fields = [
            'name',
            'genre',
            'age_aprox',
            'date_in',
            'person',
            'vaccine',
        ]

        labels = {
            'name': 'Nombre',
            'genre': 'Sexo',
            'age_aprox': 'Edad aproximada',
            'date_in': 'Fecha de rescate',
            'person': 'Adoptante',
            'vaccine': 'Vacunas',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'age_aprox': forms.TextInput(attrs={'class': 'form-control'}),
            'date_in': forms.DateInput(attrs={'class': 'form-control'}),
            'person': forms.Select(attrs={'class': 'form-control'}),
            'vaccine': forms.CheckboxSelectMultiple(),
        }
