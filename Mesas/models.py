from django.db import models

class Mesas(models.Model):
    id_mesa = models.IntegerField(primary_key=True)
    num_mesa = models.IntegerField()
    disponible_mesa = models.IntegerField()