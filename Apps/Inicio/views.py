import os

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.views import generic
from .models import Usuario
from django.contrib.auth import logout


# Create your views here.
class Inicio(generic.TemplateView):
    template_name = 'index.html'

class Nosotros(generic.TemplateView):
    template_name = 'inicio/nosotros.html'

class Servicios(generic.TemplateView):
    template_name = 'inicio/servicio.html'

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

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('inicio')

class RegistroUsuario(CreateView):
    model = User
    form_class = RegistroForm

    template_name = 'inicio/register.html'
    # success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)

        return redirect('/person/')


