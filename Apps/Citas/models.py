from django.db import models

# Create your models here.

class Citas(models.Model):
    Cedula = models.IntegerField()
    Nombre = models.TextField()
    FechaCita = models.DateTimeField()
    Correo = models.TextField(max_length=125)
    Celular = models.BigIntegerField()
    estado =models.BooleanField(default=True)

