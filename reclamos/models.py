from django.db import models
from poliza.models import (
    Poliza,
)  # Asegúrate de que el modelo Poliza esté en el mismo archivo o ajusta el import


class Reclamo(models.Model):
    no_poliza = models.ForeignKey(
        Poliza, on_delete=models.CASCADE
    )  # Clave foránea a Poliza
    no_incidente = models.CharField(max_length=8, primary_key=True)
    fecha_incidente = models.DateField()
    descripcion_r = models.CharField(max_length=100)
    monto_reclamo = models.FloatField()
    estado_reclamo = models.CharField(max_length=15)

    def __str__(self):
        return f"Reclamo {self.no_incidente} - Póliza {self.no_poliza}"
