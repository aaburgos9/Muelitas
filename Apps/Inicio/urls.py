from django.urls import path
from .views import CrearCita

app_name = 'cita'
urlpatterns = [
    path('CrearCita/', CrearCita.as_view(), name='CrearCita'),
]
