from django.shortcuts import render, redirect
import os
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from utils import render_to_pdf
from django.contrib.auth import logout
from django.contrib import messages
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views import generic
from .models import Usuario,Historial_clinico
from .forms import FormHistorial
from bootstrap_modal_forms.generic import (BSModalUpdateView,BSModalDeleteView,BSModalCreateView)
from django.views.generic.edit import FormView


#class Muelitas(generic.TemplateView):
 #      template_name = 'index.html'


class Nosotros(generic.TemplateView):
    template_name = 'Muelitas/nosotros.html'

class Servicios(generic.TemplateView):
    template_name = 'Muelitas/servicio.html'


class info_odontologo(generic.TemplateView):
    template_name = 'odontologo/info_odontologo.html'


#class Perfil(generic.TemplateView):
#    model = Usuario
#    template_name = 'Muelitas/perfil.html'
#    queryset = Usuario.objects.all
#
#    def get_object(self):
#        id_ = self.kwargs.get("pk")
#        return get_object_or_404(Usuario, id=id_)


class eliminarRegistro(generic.DeleteView):
    model = Usuario
    success_url = reverse_lazy('Muelitas:listarRegistro')



class CrearHistorial(generic.CreateView):
    model = Historial_clinico
    form_class = FormHistorial
    template_name = 'Muelitas/crear_historia.html'
    success_url = reverse_lazy('Muelitas:listarHistorial')

class listarHistorial(generic.ListView):
    model = Historial_clinico
    context_object_name = 'history'
    queryset = Historial_clinico.objects.all
    template_name = ('Muelitas/listar_historial.html')


# Create your views here.
def inicio(request):
        return render(request, 'index.html')

def principal(request):
        return render(request, 'Muelitas/principal.html')

def formularioLogin(request,msn):
    contexto = {'msn': msn}
    return render(request, 'Muelitas/formulario_login.html',contexto)



def login(request):
        try:
                documento= request.POST['documento']
                password = request.POST['password']
                # verificar si hay un usuario con ese usuario y contraseña
                q = Usuario.objects.get(Documento = documento, Password = password)
                request.session['logueado'] =[q.Nombre, q.Documento, q.Password, q.rol, q.id]
                if q.rol == '1':
                #en caso afirmativo, creo la variable de sesion
                        return HttpResponseRedirect(reverse('calendario:calendar', args=()))
                elif q.rol == '2':

                        request.session['logueado'] =[q.Nombre, q.Documento, q.Password, q.rol]
                        return HttpResponseRedirect(reverse('calendario:calendar', args=()))
                elif q.rol == '3':
                    #Paciente
                        request.session['logueado'] =[q.Nombre, q.Documento, q.Password, q.rol]
                        return HttpResponseRedirect(reverse('calendario:calendar', args=())
                        )
                else:
                        return render(request, 'Muelitas/formulario_login.html')
        except Exception as e:
            return HttpResponseRedirect(reverse('Muelitas:formularioLogin',args=(e,)))




def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada Exitosamente')
    return redirect('/')



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

        return HttpResponseRedirect(reverse('Muelitas:login', args=('')))
    except Exception as e:
       return HttpResponseRedirect(reverse('Muelitas:formularioRegistro', args=(e,)))




def ListarRegistro(request):
        ses = request.session.get('logueado',False)
        if ses:
                q = Usuario.objects.all()
                contexto = {'Usuario': q }

                return render(request, 'Muelitas/formulario_listar.html', contexto)
        else:
                return HttpResponse("No tiene permisos para ver el listado")




def EditarRegistro(request, id):
        q = Usuario.objects.get(pk=id)
        contexto = {'datos': q }
        return render(request, 'Muelitas/formulario_editar.html', contexto)



def Perfil(request):
        ses = request.session.get('logueado',False)
        n= Usuario.objects.get(Documento = ses[1])
        contexto = {'datos': n}
        return render(request, 'Muelitas/perfil.html', contexto)



def actualizarRegistro(request):
        try:
                id = request.POST['id']
                q = Usuario.objects.get(pk=id)
                q.Documento = request.POST['Documento']
                q.Nombre = request.POST['Nombre']
                q.Password = request.POST['Password']
                q.Correo = request.POST['Correo']
                q.rol = request.POST['rol']
                q.Estado = request.POST['Estado']

                q.save()
                return HttpResponseRedirect(reverse('Muelitas:listarRegistro', args=()))
        except Exception as e:
                return HttpResponse(e)


def verRegistro(request, id):
    try:
        q = Usuario.objects.get(pk=id)
        diccionario = model_to_dict(q)
        return JsonResponse(diccionario)
    except Exception as e:
        return HttpResponse(e)

def reportepdf(request):
        q= Historial_clinico.objects.all()
        contexto = {'history': q }
        pdf= render_to_pdf('Muelitas/historia_clinica.html', contexto)
        response = HttpResponse(pdf, content_type='application/pdf')
        #para abrir el pdf directamente
        response ['content-Disposition'] = 'filename=Reporte.pdf'
        #para descargar directamente
        #response ['content-Disposition'] = 'attachment;filename=Reporte.pdf'
        return response



#def eliminarRegistro(request, id):
#        try:
#                q = Usuario.objects.get(pk=id)
#                q.Estado = 'False'
#                q.save()
#                contexto = {'Usuarios': q }
#                #return HttpResponseRedirect(reverse('Muelitas:listarRegistro', args=()))
#                return render(request, 'Muelitas/formulario_listar.html', contexto)
#
#        except Exception as e:
#                return HttpResponse(e)