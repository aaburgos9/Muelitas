from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password1',
            'password2',
        ]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control form-control-user', 'type': 'email', 'placeholder': 'Email'}),
            'password1': forms.TextInput(
                attrs={'class': 'form-control form-control-user', 'placeholder': 'Contraseña'}),
            'password2': forms.TextInput(
                attrs={'class': 'form-control form-control-user', 'placeholder': 'Confirmar contraseña'}),
        }

        labels = {
            'email' : 'Usuario / Email' ,
            'password1': 'Contraseña',
            'password2' : 'Confirmar contraseña',

        }


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
