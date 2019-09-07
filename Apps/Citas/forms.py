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
