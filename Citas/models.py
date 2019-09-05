from django.db import models

# Create your models here.

class Citas:
    fecha = models.DateTimeField()
    correo = models.TextField(max_length=125)
    celular = models.IntegerField()
