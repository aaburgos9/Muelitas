from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from .models import Citas, Multas
from .forms import FormCita, FormMultas
from bootstrap_modal_forms.generic import (BSModalUpdateView,BSModalDeleteView,BSModalCreateView)
from django.template.loader import render_to_string

from django.core.mail import EmailMessage



# Create your views here.
class CrearCita(BSModalCreateView):
        model = Citas
        form_class = FormCita
        template_name = 'index.html'
        success_url = reverse_lazy('cita:CrearCita')





class ListarCitas(generic.ListView):
    model = Citas
    template_name = ('calendar.html')
    context_object_name = 'Citas'
    queryset = Citas.objects.all



class contacto(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['contact_form'] =  FormCita
        return context

    def post(self, request, *args, **kwargs):
        Documento = request.POST.get('Documento')
        Nombre = request.POST.get('Nombre')
        Horacita = request.POST.get('Horacita')
        FechaCita = request.POST.get('FechaCita')
        Correo = request.POST.get('Correo')
        Celular = request.POST.get('Celular')


        body = render_to_string(
            'Citas/corro.html', {
                'Documento': Documento,
                'Nombre': Nombre,
                'Horacita': Horacita,
                'FechaCita': FechaCita,
                'Correo': Correo,
                'Celular': Celular,
            },
        )
        email_message = EmailMessage(
            subject='Mensaje de usuario',body=body,from_email=Correo,to=["asdental495@gmail.com"],
        )
        email_message.content_subtype = 'html'
        email_message.send()

        return HttpResponseRedirect(reverse('cita:CrearCita'))






class EditarCitas(BSModalUpdateView):
    model = Citas
    form_class = FormCita
    template_name = 'Citas/edit.html'   
    success_url = reverse_lazy('cita:listar')


class EliminarCitas(generic.DeleteView):
    model = Citas   
    success_url = reverse_lazy('cita:listar')


class DetalleCitas(generic.DeleteView):
    model = Citas
    template_name = 'Citas/ver_citas.html'
    queryset = Citas.objects.all

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Citas, id=id_)


class CrearMulta(generic.CreateView):
    model = Multas
    form_class = FormMultas
    template_name = 'Citas/crear_multas.html'
    success_url = reverse_lazy('cita:listarMultas')


class ListarMultas(generic.ListView):
    model = Multas
    template_name = ('Citas/consultar_multas.html')
    context_object_name = 'Multa'
    queryset = Multas.objects.all