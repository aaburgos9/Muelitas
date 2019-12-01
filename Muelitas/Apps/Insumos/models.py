from django.db import models



class Producto(models.Model):
    Nombre = models.CharField(max_length=45)
    Precio = models.IntegerField()
    cantidad = models.IntegerField()
    Proveedor = models.CharField(max_length=45)

    def __str__(self):
        return '{}'.format(self.Nombre)
