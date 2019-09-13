from django import forms
from .models import Citas


class FormCita(forms.ModelForm):
    class Meta:
        model = Citas
        fields = [
            'Cedula',
            'Nombre',
            'FechaCita',
            'Correo',
            'Celular',
        ]
        widgets = {
            'Cedula': forms.TextInput(
                attrs={'class': 'form-control ', 'type': 'number', 'placeholder': 'Cedula'}),
            'Nombre': forms.TextInput(
                attrs={'class': 'form-control ',  'placeholder': 'Nombre'}),
            'FechaCita': forms.TextInput(
                attrs={'class': 'form-control ', 'type': 'date','placeholder': 'fecha'}),
            'Correo': forms.TextInput(
                attrs={'class': 'form-control ','type': 'email', 'placeholder': 'correo'}),
            'Celular': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Celular'}),
        }
