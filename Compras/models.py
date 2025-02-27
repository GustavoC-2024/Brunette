from django.db import models
from Cajas.models import Caja
from Proveedores.models import Proveedores
from Productos.models import Productos
from django.core.exceptions import ValidationError

class Compras(models.Model):
    id_comp = models.IntegerField(primary_key=True)
    id_caja = models.ForeignKey(Caja, models.DO_NOTHING, db_column='id_caja')
    id_prov = models.ForeignKey(Proveedores, models.DO_NOTHING, db_column='id_prov')
    fecha_hora_comp = models.DateTimeField(auto_now_add=True)
    monto_comp = models.FloatField()
    nro_comp = models.IntegerField()

    def clean(self):
        if not self.id_caja.abierta_caja:
            raise ValidationError('La caja está cerrada. No se puede registrar la compra.')
        
class DetalleCompras(models.Model):
    id_det_comp = models.IntegerField(primary_key=True)
    id_comp = models.ForeignKey(Compras, models.DO_NOTHING, db_column='id_comp')
    id_prod = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_prod')
    cantidad_prod_comp = models.IntegerField()
    precio_uni_prod = models.FloatField()
    sub_total_comp = models.FloatField()
    total_comp = models.FloatField()