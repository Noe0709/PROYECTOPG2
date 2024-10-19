from django.db import models
from poliza.models import (
    Poliza,
)  # Asegúrate de que el modelo Poliza esté en el mismo archivo o ajusta el import


class Pago(models.Model):
    pago_id = models.CharField(max_length=8, primary_key=True)
    no_poliza = models.ForeignKey(
        Poliza, on_delete=models.CASCADE
    )  # Clave foránea a Poliza
    monto_pago_recurrente = models.FloatField()
    metodo_pago = models.CharField(max_length=25)
    fecha_pago = models.DateField()
    descrip_pago = models.CharField(max_length=125)

    def __str__(self):
        return f"Pago {self.pago_id} - Póliza {self.no_poliza}"
