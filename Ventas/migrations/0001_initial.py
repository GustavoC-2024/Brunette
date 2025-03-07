# Generated by Django 5.1.5 on 2025-02-06 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cajas', '0001_initial'),
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_venta', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField()),
                ('hora_venta', models.TimeField()),
                ('total_venta', models.FloatField()),
                ('venta_realizada', models.IntegerField()),
                ('id_caja', models.ForeignKey(db_column='id_caja', on_delete=django.db.models.deletion.DO_NOTHING, to='Cajas.caja')),
                ('id_cli', models.ForeignKey(db_column='id_cli', on_delete=django.db.models.deletion.DO_NOTHING, to='Clientes.clientes')),
            ],
        ),
    ]
