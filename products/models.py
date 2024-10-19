from django.db import models


# Create your models here.
class Producto(models.Model):
    producto_cod = models.CharField(max_length=8, primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    tipo_producto = models.CharField(max_length=50)
    tipo_siniestro = models.CharField(max_length=35)
    descripcion_siniestro = models.CharField(max_length=150)
    monto_estimado = models.FloatField()
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.producto_cod
