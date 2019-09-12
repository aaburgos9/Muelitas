import os
from django.template.loader import get_template
#from utils import render_to_pdf
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import generic
from .models import Usuario


# Create your views here.
class Inicio(generic.TemplateView):
    template_name = 'index.html'

class Principal(generic.TemplateView):
    template_name = 'secretaria/principal.html' 

def login(request):
        try:
                documento= request.POST['documento']
                password = request.POST['password']
                # verificar si hay un usuario con ese usuario y contraseña
                q = Usuario.objects.get(Documento = documento, Password = password)
                #en caso afirmativo, creo la variable de sesion
                request.session['logueado'] =[]
                return HttpResponseRedirect(reverse('inicio:principal', args=()))
        except Exception as e:
                return HttpResponse(e)

