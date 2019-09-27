from django.urls import path
from .views import Principal,login ,logoutUsuario ,Nosotros ,Servicios
from django.contrib.auth.decorators import login_required

app_name = 'inicio'
urlpatterns = [
    path('principal/', Principal.as_view(), name='principal'), 
    path('login/', login, name='login'),
    path('register/', views.RegistroUsuario.as_view(), name='register'),
    path('logout/', login_required(logoutUsuario), name="logout"),
    path('nosotros', Nosotros.as_view(), name='nosotros'),
    path('Servicios', Servicios.as_view(), name='Servicios'),
]
