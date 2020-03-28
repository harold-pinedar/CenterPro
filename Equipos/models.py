from django.db import models

# Create your models here.

class TipoEquipo(models.Model):
    id_tipo_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Nombre Equipo.", max_length=150)
    descripcion = models.TextField(verbose_name="Descripción.")

    def __str__(self):
        return self.nombre


class Marcas(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name="Nombre Marca.", max_length=150)
    descripcion = models.TextField(verbose_name="Descripción")
    id_tipo_equipo = models.ForeignKey(TipoEquipo, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre
        
class Modelos(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    id_marca = models.ForeignKey(Marcas, null=True, on_delete=models.SET_NULL)
    modelo = models.CharField(verbose_name="Modelo.", max_length=200)

    def __str__(self):
        return self.modelo