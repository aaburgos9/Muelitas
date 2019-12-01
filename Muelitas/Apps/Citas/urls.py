from django.urls import path
from .views import CrearCita, ListarCitas,EditarCitas,EliminarCitas,DetalleCitas,CrearMulta, ListarMultas,contacto
from . import views


app_name = 'cita'
urlpatterns = [
    path('CrearCita/', CrearCita.as_view(), name='CrearCita'),
    path('listar/', ListarCitas.as_view(), name='listar'),
    path('contato/', contacto.as_view(), name='contacto'),

   # path('formCita/<str:msn>/', views.ForCita, name='formuCita'),
    path('listarMultas/', ListarMultas.as_view(), name='listarMultas'),
    path('editar/<int:pk>/', EditarCitas.as_view(), name='editar'),
    path('eliminar/<int:pk>/', EliminarCitas.as_view(), name='eliminarCita'),
    path('detalle/<int:pk>/', DetalleCitas.as_view(), name='detalle'),
    path('CrearMulta/', CrearMulta.as_view(), name='CrearMulta'),


]
