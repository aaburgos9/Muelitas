from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'Nombre',
            'Precio',
            'cantidad',
            'Proveedor',

        ]
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'Autofocus': True}),
            'Precio': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'Proveedor': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
