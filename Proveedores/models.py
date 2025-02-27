from django.db import models

class Proveedores(models.Model):
    id_prov = models.IntegerField(primary_key=True)
    nombre_prov = models.CharField(max_length=50)
    tipo_prov = models.CharField(max_length=50)
    telefono_prov = models.IntegerField(blank=True, null=True)
    correo_prov = models.CharField(max_length=50, blank=True, null=True)
    direccion_prov = models.CharField(max_length=50)