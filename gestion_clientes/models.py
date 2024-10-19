from django.db import models


# Create your models here.
class Cliente(models.Model):
    SEXO_CHOICES = [
        ("Hombre", "Hombre"),
        ("Mujer", "Mujer"),
    ]
    cod_cliente = models.CharField(max_length=8, null=True)
    nombre_completo = models.CharField(max_length=100, null=True)
    edad = models.IntegerField(null=True)
    nit = models.CharField(max_length=15, null=True)
    dpi = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=35, null=True)
    descripcion_cliente = models.CharField(max_length=10, null=True)
    sexo = models.CharField(
        max_length=6, choices=SEXO_CHOICES, null=True
    )  # Campo con opciones
    direccion_completa = models.CharField(max_length=100, null=True)
    departamento = models.CharField(max_length=25)
    municipio = models.CharField(max_length=50)
    telefono_1 = models.CharField(max_length=8, null=True)
    telefono_2 = models.CharField(max_length=8, blank=True, null=True)
    profesion = models.CharField(max_length=30, null=True)
    fecha_nacimiento = models.DateField(null=True)
    estado_civil = models.CharField(max_length=20, blank=True, null=True)
    ingresos_mensuales_prom = models.FloatField(null=True)

    def __str__(self):
        return self.nombre_completo


class HistorialCliente(models.Model):
    cliente = models.ForeignKey(
        Cliente, related_name="historial", on_delete=models.CASCADE
    )
    descripcion = models.TextField()
    fecha_interaccion = models.DateTimeField()

    def __str__(self):
        return f"Interacción con {self.cliente.nombre} el {self.fecha_interaccion}"
