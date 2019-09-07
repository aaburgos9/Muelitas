from django.shortcuts import render
from django.views import generic


# Create your views here.
class Inicio(generic.TemplateView):
    template_name = 'index.html'