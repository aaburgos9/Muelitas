from django.db import models
from Apps.calendario.models import Events

# Create your models here.


class Citas(models.Model):
       Documento = models.IntegerField()
       Nombre = models.TextField()
       FechaCita = models.DateField()
       hora= (('0', 'Hora'),
              ('1', '7:00 am'),
              ('2', '8:00 am'),
              ('3', '9:00 am'),
              ('4', '10:00 am'),
              ('5', '11:00 am'),
              ('6', '12:00 pm'),
              ('7', '1:00 pm'),
              ('8', '2:00 pm'),
              ('9', '3:00 pm'),
              ('10', '4:00 pm'),
              ('11', '5:00 pm'),
              )
       Horacita=models.CharField(max_length=1, choices=hora, default='0')
       Correo = models.TextField(max_length=125)
       Celular = models.BigIntegerField()
       estado =models.BooleanField(default=True)

       def  __str__(self):
              return'{}'.format(self.Horacita)


class Multas(models.Model):
       Documento = models.IntegerField()
       Nombre = models.TextField(max_length=125)
       FechaMulta = models.ForeignKey(Events, on_delete=models.CASCADE)
       ValorMulta = models.IntegerField()
       estado = models.BooleanField(default=True)
