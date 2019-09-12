from django.shortcuts import render
from django.views import generic
from Inicio.models import Usuario


# Create your views here.
class Inicio(generic.TemplateView):
    template_name = 'index.html'

def login(request):
        try:
                documento= request.POST['documento']
                password = request.POST['contraseña']
                # verificar si hay un usuario con ese usuario y contraseña
                q = Usuario.objects.get(documento = documento, contraseña = password)
                #en caso afirmativo, creo la variable de sesion
                request.session['logueado'] =[q.nombre, q.apellido, q.id, q.rol]
                return HttpResponseRedirect(reverse('citas:secretaria/principal.html', args=()))
        except Exception as e:
                return HttpResponse(e)