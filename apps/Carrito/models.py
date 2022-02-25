from django.db import models

# ---------------------------------------------------------
# PRODUCTO


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
