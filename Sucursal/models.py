from django.db import models
from Empresa.models import Empresas

# Create your models here.

class Sucursal(models.Model):
    id_sucursal = models.CharField(verbose_name="Id Empresa.", max_length=100, primary_key=True) 
    id_empresa = models.ForeignKey(Empresas, null=True, on_delete=models.CASCADE)
    nombre_sucursal = models.CharField(verbose_name="Nombre Socursal.", max_length=255) 
    direccion = models.CharField(verbose_name="Direccion.", max_length=255, blank=True)
    coordenadas = models.CharField(verbose_name="Coordenadas", max_length=255, blank=True) 
    telefono = models.CharField(verbose_name="Telefono Contacto", max_length=255) 
    email =  models.EmailField()
    logo =   models.ImageField(blank=True, null=True) 
    regimenes = {
        ("C", "Común"), 
        ("S", "Simplificado")
    }
    regimen =  models.CharField(max_length=2, choices=regimenes, default="C")
    texto_ley_st = models.CharField(max_length=255)
    texto_ley_ventas = models.CharField(max_length=255)  

    def __str__(self):
        return self.nombre_sucursal