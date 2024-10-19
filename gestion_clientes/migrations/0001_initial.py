# Generated by Django 5.1.1 on 2024-10-01 03:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_cliente', models.CharField(max_length=8, null=True)),
                ('nombre_completo', models.CharField(max_length=100, null=True)),
                ('edad', models.IntegerField(null=True)),
                ('nit', models.CharField(max_length=15, null=True)),
                ('dpi', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=35, null=True)),
                ('descripcion_cliente', models.CharField(max_length=10, null=True)),
                ('sexo', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=6, null=True)),
                ('direccion_completa', models.CharField(max_length=100, null=True)),
                ('departamento', models.CharField(max_length=25)),
                ('municipio', models.CharField(max_length=50)),
                ('telefono_1', models.CharField(max_length=8, null=True)),
                ('telefono_2', models.CharField(blank=True, max_length=8, null=True)),
                ('profesion', models.CharField(max_length=30, null=True)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('estado_civil', models.CharField(blank=True, max_length=20, null=True)),
                ('ingresos_mensuales_prom', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha_interaccion', models.DateTimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historial', to='gestion_clientes.cliente')),
            ],
        ),
    ]
