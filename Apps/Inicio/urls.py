from django.urls import path
from .views import Principal,login

app_name = 'inicio'
urlpatterns = [
    path('principal/', Principal.as_view(), name='principal'), 
    path('login/', login, name='login'),
]
