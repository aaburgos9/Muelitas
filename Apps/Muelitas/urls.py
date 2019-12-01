from django.urls import path
from .views import Nosotros,Servicios,eliminarRegistro,CrearHistorial , info_odontologo,listarHistorial
from . import views

app_name = 'Muelitas'
urlpatterns = [
    
    path('inicio/', views.inicio, name='inicio'),
    path('principal/', views.principal, name='principal'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('formularioLogin/<str:msn>/', views.formularioLogin, name='formularioLogin'),

    path('formularioRegistro/<str:msn>/', views.formularioRegistro, name='formularioRegistro'),
    path('usuarioGuardar/', views.usuarioGuardar, name='usuarioGuardar'),
    path('listarRegistro/', views.ListarRegistro, name='listarRegistro'),
    path('editarRegistro/<int:id>', views.EditarRegistro, name='editarRegistro'),
    path('actualizarRegistro/', views.actualizarRegistro, name='actualizarRegistro'),
    path('verRegistro/<int:id>', views.verRegistro, name='verRegistro'),
    path('eliminarRegistro/<int:pk>', eliminarRegistro.as_view(), name='eliminarRegistro'),
    path('nosotros/', Nosotros.as_view(), name='nosotros'),
    path('Servicios/', Servicios.as_view(), name='Servicios'),
    path('info/', info_odontologo.as_view(), name='info'),
    path('Perfil/', views.Perfil, name='Perfil'),
    path('reportepdf', views.reportepdf, name='reportepdf'),
    path('CrearHistorial/', CrearHistorial.as_view(), name='CrearHistorial'),
    path('history/',listarHistorial.as_view(), name='history'),
    
]