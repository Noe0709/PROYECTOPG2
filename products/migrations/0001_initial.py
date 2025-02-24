# Generated by Django 5.1.1 on 2024-10-01 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('producto_cod', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=50)),
                ('tipo_producto', models.CharField(max_length=50)),
                ('tipo_siniestro', models.CharField(max_length=35)),
                ('descripcion_siniestro', models.CharField(max_length=150)),
                ('monto_estimado', models.FloatField()),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('actualizado_en', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
