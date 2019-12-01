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
            'Nombre': forms.TextInput(
            attrs={'class': 'form-control ', 'type': 'text',  'placeholder': 'Nombre'}),
            'Precio': forms.NumberInput(
            attrs={'class': 'form-control ', 'type': 'number', 'id': 'documento', 'placeholder': 'Precio'}),
            'cantidad': forms.NumberInput(
            attrs={'class': 'form-control ', 'type': 'number', 'id': 'documento', 'placeholder': 'Cantidad'}),
            'Proveedor': forms.TextInput(
            attrs={'class': 'form-control ', 'type': 'text', 'id': 'documento', 'placeholder': 'Proveedor'}),
            #'Nombre': forms.TextInput(attrs={'class': 'form-control', }),
            #'Precio': forms.NumberInput(attrs={'class': 'form-control', #'required': True}),
            #'cantidad': forms.NumberInput(attrs={'class': 'form-control', #'required': True}),
            #'Proveedor': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
