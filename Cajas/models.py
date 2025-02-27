from django.db import models
from Empleados.models import Empleados

class Caja(models.Model):
    id_caja = models.AutoField(primary_key=True)
    id_empl = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='id_empl')
    abierta_caja = models.IntegerField(default=0) # 0 = Cerrada, 1 = Abierta
    fecha_hs_aper_caja = models.DateTimeField(auto_now_add=True)
    fecha_hs_cier_caja = models.DateTimeField(null=True, blank=True)
    monto_inicial_caja = models.FloatField()
    total_ingresos_caja = models.FloatField(null=True, blank=True)
    total_egresos_caja = models.FloatField(null=True, blank=True)
    saldo_caja = models.FloatField(null=True, blank=True)