from django.db import models

class Clientes(models.Model):
    id_cli = models.IntegerField(primary_key=True)
    nombre_cli = models.CharField(max_length=100)
    apellido_cli = models.CharField(max_length=100)
    cuit_cli = models.IntegerField()
    tel_cli = models.IntegerField(blank=True, null=True)