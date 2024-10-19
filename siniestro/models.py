from django.db import models
from poliza.models import (
    Poliza,
)  # Asegúrate de que el modelo Poliza esté en el mismo archivo o ajusta el import


class Siniestro(models.Model):
    id_siniestro = models.CharField(max_length=8, primary_key=True)
    no_poliza = models.ForeignKey(
        Poliza, on_delete=models.CASCADE
    )  # Clave foránea a Poliza
    fecha_siniestro = models.DateField()
    tipo_siniestro = models.CharField(max_length=35)
    descripcion_siniestro = models.CharField(max_length=150)
    monto_estimado = models.FloatField()

    def __str__(self):
        return f"Siniestro {self.id_siniestro} - Póliza {self.no_poliza}"
