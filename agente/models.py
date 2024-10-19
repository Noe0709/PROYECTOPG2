from django.db import models


class Agente(models.Model):
    no_empleado = models.CharField(max_length=5, primary_key=True)
    nombre_agente = models.CharField(max_length=50)
    apellido_agente = models.CharField(max_length=50)
    telefono_ext = models.CharField(max_length=12)
    email_agente = models.EmailField(max_length=75)
    ubicacion_area = models.CharField(max_length=25)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f"{self.nombre_agente} {self.apellido_agente}"
