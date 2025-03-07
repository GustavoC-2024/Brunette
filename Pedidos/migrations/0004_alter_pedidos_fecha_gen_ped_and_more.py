# Generated by Django 5.1.5 on 2025-02-28 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cajas', '0003_alter_caja_saldo_caja_alter_caja_total_egresos_caja_and_more'),
        ('Empleados', '0001_initial'),
        ('Pedidos', '0003_alter_pedidos_id_pedido'),
        ('Ventas', '0003_detalleventa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='fecha_gen_ped',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='generado_ped',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='hora_gen_ped',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='id_caja',
            field=models.ForeignKey(db_column='id_caja', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Cajas.caja'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='id_empl',
            field=models.ForeignKey(db_column='id_empl', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Empleados.empleados'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='id_venta',
            field=models.ForeignKey(db_column='id_venta', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Ventas.ventas'),
        ),
    ]
