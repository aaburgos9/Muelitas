from django import forms

from .models import Citas,Multas
from bootstrap_modal_forms.forms import BSModalForm




class FormCita(BSModalForm):
    class Meta:
        model = Citas
        hora = (('0', 'Hora'),
                ('1', '7:00 am'),
                ('2', '8:00 am'),
                ('3', '9:00 am'),
                ('4', '10:00 am'),
                ('5', '11:00 am'),
                ('6', '12:00 pm'),
                ('7', '1:00 pm'),
                ('8', '2:00 pm'),
                ('9', '3:00 pm'),
                ('10', '4:00 pm'),
                ('11', '5:00 pm'),
                )
        fields = [
            'Documento',
            'Nombre',
            'FechaCita',
            'Horacita',
            'Correo',
            'Celular',
        ]
        widgets = {
            'Documento': forms.TextInput(
                attrs={'class': 'form-control ', 'type': 'number', 'id': 'documento', 'placeholder': 'Documento' ,'name': 'Docuemnto'}),
            'Nombre': forms.TextInput(
                attrs={'class': 'form-control ',  'placeholder': 'Nombre' ,'name': 'Nombre'}),
            'FechaCita': forms.TextInput(
                attrs={'class': 'form-control ', 'type': 'date','placeholder': 'fecha' ,'name': 'FechaCita'}),
            'Horacita': forms.Select(attrs={'class': 'form-control' ,'name': 'Horacita'}),
            'Correo': forms.TextInput(
                attrs={'class': 'form-control ','type': 'email', 'placeholder': 'correo' ,'name': 'correo'}),
            'Celular': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Celular' ,'name': 'Celular'})
        }


class FormMultas(forms.ModelForm):
    class Meta:
        model = Multas
        fields = [
            'Documento',
            'Nombre',
            'FechaMulta',
            'ValorMulta'
        ]

        widgets = {
            'Documento': forms.TextInput(
                attrs={'class': 'form-control ', 'type': 'number', 'id': 'documento', 'placeholder': 'Documento'}),
            'Nombre': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Nombre'}),
            'FechaMulta': forms.TextInput(
                attrs={'class': 'form-control ', 'type': 'date','placeholder': 'fecha multa'}),
            'ValorMulta': forms.NumberInput(
                attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'valor multa'})
        }