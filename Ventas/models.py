from django.db import models
from Clientes.models import Clientes
from Cajas.models import Caja
from Productos.models import Productos
from django.core.exceptions import ValidationError

class Ventas(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    id_cli = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cli')
    id_caja = models.ForeignKey(Caja, models.DO_NOTHING, db_column='id_caja')
    fecha_venta = models.DateField(auto_now_add=True)
    hora_venta = models.TimeField(auto_now_add=True)
    total_venta = models.FloatField()
    venta_realizada = models.IntegerField()

    def clean(self):
        if not self.id_caja.abierta_caja:
            raise ValidationError('La caja está cerrada. No se puede registrar la venta.')

class DetalleVenta(models.Model):
    id_det_venta = models.IntegerField(primary_key=True)
    id_venta = models.ForeignKey(Ventas, models.DO_NOTHING, db_column='id_venta')
    id_prod = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_prod')
    cantidad_prod_venta = models.IntegerField()
    subtotal_det = models.FloatField()
    precio_unitario = models.FloatField()