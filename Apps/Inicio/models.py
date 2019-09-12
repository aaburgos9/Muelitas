from django.db import models

# Create your models here.


class Usuario(models.Model):
    Documento = models.IntegerField()
    Nombre = models.TextField(max_length=125)
    Password= models.TextField(max_length=125)
    Correo = models.TextField(max_length=125)
    estado =models.BooleanField(default=True)