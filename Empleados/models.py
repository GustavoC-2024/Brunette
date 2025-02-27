from django.db import models

class Empleados(models.Model):
    id_empl = models.IntegerField(primary_key=True)
    dni_empl = models.IntegerField()
    nombre_empl = models.CharField(max_length=50)
    apellido_empl = models.CharField(max_length=50)
    domicilio_empl = models.CharField(max_length=50)
    telefono_empl = models.IntegerField(blank=True, null=True)
    correo_empl = models.CharField(max_length=50, blank=True, null=True)