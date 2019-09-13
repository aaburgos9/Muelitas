from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Citas
from .forms import FormCita


# Create your views here.
class CrearCita(generic.CreateView):
    model = Citas
    form_class = FormCita
    template_name = 'Citas/form.html'
    success_url = reverse_lazy('Citas:listar')

class ListarCitas(generic.ListView):
    model = Citas
    template_name = ('Citas/list.html')
    context_object_name = 'Citas'
    queryset = Citas.objects.all