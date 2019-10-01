from django.shortcuts import render
import os
from django.template.loader import get_template
#from utils import render_to_pdf
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views import generic
from .models import Usuario
from django.views.generic.edit import FormView


class Muelitas(generic.TemplateView):
        template_name = 'index.html'

class Nosotros(generic.TemplateView):
    template_name = 'inicio/nosotros.html'

class Servicios(generic.TemplateView):
    template_name = 'inicio/servicio.html'

# Create your views here.
def index(request,msn):
        contexto={'mensaje':msn}
        return render(request, 'Muelitas/index.html', contexto)

def principal(request):
        return render(request, 'Muelitas/principal.html')

def formularioLogin(request):
        return render(request, 'Muelitas/formulario_login.html')



def login(request):
        try:
                documento= request.POST['documento']
                password = request.POST['password']
                # verificar si hay un usuario con ese usuario y contraseña
                q = Usuario.objects.get(Documento = documento, Password = password)
                #en caso afirmativo, creo la variable de sesion
                request.session['logueado'] =[q.Documento, q.Password]
                return HttpResponseRedirect(reverse('Muelitas:principal', args=()))
        except Exception as e:
                return HttpResponse(e)
                        
def logout(request):
        
        try:
                
                 
                return HttpResponseRedirect(reverse('Muelitas/index.html', arg=()))
        except Exception as e:
                return HttpResponse(e)

                
def formularioRegistro(request,msn):
        contexto =  {'msn':msn}
        return render(request,'Muelitas/formulario_registro.html',contexto)

        
def usuarioGuardar(request):
    try:
        usuario = Usuario(
            Documento = request.POST['Documento'],
            Nombre = request.POST['Nombre'],
            Password = request.POST['Password'],
            Correo = request.POST['Correo'], 
        )
        usuario.save()
        
        return HttpResponseRedirect(reverse('Muelitas:principal', args=()))
    except Exception as e:
       return HttpResponseRedirect(reverse('Muelitas:formularioRegistro', args=(e,)))
