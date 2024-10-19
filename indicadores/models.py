from django.db import models
from gestion_clientes.models import Cliente


class Indicador(models.Model):
    id_ci = models.CharField(max_length=10, primary_key=True)
    cod_cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, db_column="cod_cliente"
    )
    antiguedad_cte_anos = models.IntegerField()
    antiguedad_cte_meses = models.IntegerField()
    probabilidad_vida_se_mortal = models.IntegerField()
    enfermedades_previas = models.CharField(max_length=90)
    detalle_enfermedad = models.CharField(max_length=100, blank=True, null=True)
    familiar_enfermedad = models.CharField(max_length=90)

    def __str__(self):
        return f"Indicador {self.id_ci} - Cliente {self.cod_cliente}"
