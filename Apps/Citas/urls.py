from django.urls import path
from .views import CrearCita, ListarCitas

app_name = 'cita'
urlpatterns = [
    path('CrearCita/', CrearCita.as_view(), name='CrearCita'),
    path('listar/', ListarCitas.as_view(), name='listar'),
]
