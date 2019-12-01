from django.db import models


# Create your models here.
class Usuario(models.Model):
    Documento = models.BigIntegerField(unique = True)
    Nombre = models.TextField(max_length=125)
    Password= models.TextField(max_length=125)
    Correo = models.TextField(max_length=125)
    ROLES= (('2', 'odontologo'),
            ('1', 'secretaria'),
            ('3', 'paciente'))
    rol=models.CharField(max_length=1, choices=ROLES, default='3')
    Estado =models.BooleanField(default=True)

    def __str__(self):
            return '{}'.format(self.Documento)


class Historial_clinico(models.Model):
        Documento = models.BigIntegerField(unique = True)
        Nombre = models.TextField(max_length=125)
        TipoSexo =(('0', 'sexo'),
                ('1','Femenino'),
                ('2', 'Masculino')) 
        sexo= models.CharField(max_length=1, choices=TipoSexo, default='0')
        fechaNacimiento = models.DateField()
        lugarNacimiento = models.TextField(max_length=125)
        estadoC= (('0', 'estado civil'),
                ('1', 'soltero'),
                ('2', 'comprometido/a'),
                ('3', 'casado'),
                ('4', 'union libre'),
                ('5', 'divorciado/a'),
                ('6', 'viudo/a'))
        estadoCivil = models.TextField(max_length=1, choices=estadoC, default='0')
        telefono = models.BigIntegerField()
        tipoRH = (('0', 'RH'),
                ('1', 'A+'),
                ('2', 'A-'),
                ('3', 'B+'),
                ('4', 'B-'),
                ('5', 'AB+'),
                ('6', 'AB-'),
                ('7', 'O+'),
                ('8', 'O-'))
        RH = models.TextField(max_length=1, choices=tipoRH, default='0')
        ocupacion = models.TextField(max_length=125)
        motivoConsulta = models.TextField(max_length=200)