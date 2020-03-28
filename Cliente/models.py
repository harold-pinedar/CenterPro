from django.db import models
from Sucursal.models import Sucursal
# Create your models here.

class Cliente(models.Model):
    identificacion_cliente = models.CharField(verbose_name="Identificaón Cliente", max_length=20, primary_key=True, null=False, blank=False)
    nombre = models.CharField(verbose_name="Nombre Cliente", null=False, max_length=20)
    celular = models.CharField(verbose_name="Numero De Celular", max_length=10)
    email = models.EmailField()
    direeccion = models.CharField(verbose_name="Dirección", max_length=20)
    fecha_nacimientos = models.DateField()
    id_empresa = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    id_sucursal = models.ForeignKey(Sucursal, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre