from django.db import models
from Proveedores.models import Proveedores

class Productos(models.Model):
    id_prod = models.AutoField(primary_key=True)
    nombre_prod = models.CharField(max_length=50, verbose_name="Nombre")
    precio_prod = models.FloatField(verbose_name="Precio")
    stock_min_prod = models.IntegerField()
    stock_actual_prod = models.IntegerField(verbose_name="Stock actual")
    punto_reposicion_prod = models.IntegerField()
    stock_max_prod = models.IntegerField()
    existencia_insumo = models.IntegerField()
    insumo = models.IntegerField()
    
    def __str__(self):
        fila="Id: "+ str(self.id_prod) + "Nombre: " +self.nombre_prod + "-"+ "Precio:" +str(self.precio_prod) + "-" "Stock Actual: " +str(self.stock_actual_prod)
        return fila

class ProvProductos(models.Model):
    idprov_productos = models.IntegerField(primary_key=True)
    id_prov = models.ForeignKey(Proveedores, models.DO_NOTHING, db_column='id_prov')
    id_prod = models.IntegerField()
    descripcion_prod_prov = models.TextField()
    
