from django import forms
from .models import Usuario,Historial_clinico
from django.forms import ModelForm
from bootstrap_modal_forms.forms import BSModalForm 



class FormHistorial(forms.ModelForm):
    class Meta:
        model= Historial_clinico
        fields = [
            'Documento',
            'Nombre',
            'sexo',
            'fechaNacimiento',
            'lugarNacimiento',
            'estadoCivil',
            'telefono',
            'RH',
            'ocupacion',
            'motivoConsulta',
        ]

        widgets = {
            'Documento': forms.TextInput(
            attrs={'class': 'form-control ', 'type': 'number', 'id': 'documento', 'placeholder': 'Documento'}),
            'Nombre': forms.TextInput(
                attrs={'class': 'form-control ', 'type': 'text', 'placeholder': 'Nombre'}),
            'sexo': forms.Select(
                attrs={'class': 'form-control '}),
            'fechaNacimiento': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'fecha nacimiento'}),
            'lugarNacimiento' : forms.TextInput(
                attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'lugar nacimiento'}),
            'estadoCivil': forms.Select(
                attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(
                attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'telefono'}),
            'RH': forms.Select(
                attrs={'class': 'form-control'}),
            'ocupacion': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'ocupacion'}),
            'motivoConsulta': forms.Textarea(
                attrs={'class': ' form-control', 'type': 'textarea', 'placeholder': 'motivo de consulta'})              
        }

