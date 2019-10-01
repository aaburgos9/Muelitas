from django.db import models

# Create your models here.
class Usuario(models.Model):
    Documento = models.BigIntegerField()
    Nombre = models.TextField(max_length=125)
    Password= models.TextField(max_length=125)
    Correo = models.TextField(max_length=125)
    ROLES= (('1', 'secretaria'),
            ('2', 'odontologo'),
            ('3', 'paciente'))
    rol=models.CharField(max_length=1, choices=ROLES, default='3')
    Estado =models.BooleanField(default=True)
