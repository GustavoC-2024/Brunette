from django.db import models
from Mesas.models import Mesas
from Cajas.models import Caja
from Ventas.models import Ventas
from Empleados.models import Empleados
from Productos.models import Productos

class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_mesa = models.ForeignKey(Mesas, models.DO_NOTHING, db_column='id_mesa')
    id_caja = models.ForeignKey(Caja, models.DO_NOTHING, db_column='id_caja',null=True)
    id_venta = models.ForeignKey(Ventas, models.DO_NOTHING, db_column='id_venta',null=True)
    id_empl = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='id_empl',null=True)
    generado_ped = models.IntegerField(null=True)
    fecha_gen_ped = models.DateField(null=True)
    hora_gen_ped = models.TimeField(null=True)
    proceso_ped = models.IntegerField()
    fecha_pro_ped = models.DateField(blank=True, null=True)
    hora_pro_ped = models.TimeField(blank=True, null=True)
    listo_ped = models.IntegerField()
    fecha_lis_ped = models.DateField(blank=True, null=True)
    hora_lis_ped = models.TimeField(blank=True, null=True)
    entregado_ped = models.IntegerField()
    fecha_ent_ped = models.DateField(blank=True, null=True)
    hora_ent_ped = models.TimeField(blank=True, null=True)
    pagado_ped = models.IntegerField()
    fecha_pago_ped = models.TimeField(blank=True, null=True)
    tipo_pago_ped = models.CharField(max_length=50, blank=True, null=True)

class DetallePed(models.Model):
    id_det_ped = models.IntegerField(primary_key=True)
    id_pedido = models.ForeignKey(Pedidos, models.DO_NOTHING, db_column='id_pedido')
    id_prod = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_prod')
    precio_uni_ped = models.FloatField()
    cantidad_ped = models.FloatField()
    sub_total_ped = models.FloatField()
    total_ped = models.FloatField()