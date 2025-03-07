# Generated by Django 5.1.5 on 2025-02-17 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cajas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='abierta_caja',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='caja',
            name='fecha_hs_aper_caja',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='caja',
            name='fecha_hs_cier_caja',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='caja',
            name='id_caja',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
