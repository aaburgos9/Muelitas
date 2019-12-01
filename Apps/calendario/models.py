from django.db import models

from Apps.Muelitas.models import Usuario

# Create your models here.

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    #fecha de la cita
    start = models.DateField(null=True,blank=True)
    #hora de la cita
    end = models.TimeField(null=True,blank=True)
    def __str__(self):
        return self.name



