# Generated by Django 5.1.5 on 2025-02-28 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mesas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesas',
            name='disponible_mesa',
            field=models.BooleanField(default=True),
        ),
    ]
