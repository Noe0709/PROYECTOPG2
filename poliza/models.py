from django.db import models
from products.models import Producto
from agente.models import Agente
from gestion_clientes.models import Cliente


class Poliza(models.Model):
    no_poliza = models.CharField(max_length=8, primary_key=True)
    cod_cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE
    )  # Clave foránea a DatosCliente
    estado = models.CharField(max_length=15)
    fecha_fin = models.DateField()
    fecha_ingreso = models.DateField()
    monto_asegurado = models.FloatField()
    producto_cod = models.ForeignKey(
        Producto, on_delete=models.CASCADE
    )  # Clave foránea a Producto
    no_empleado = models.ForeignKey(
        Agente, on_delete=models.CASCADE
    )  # Clave foránea a Agente

    def __str__(self):
        return f"Póliza {self.no_poliza} - Cliente {self.cod_cliente}"
