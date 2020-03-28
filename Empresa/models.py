from django.db import models

# Create your models here.

class Empresas(models.Model):
    id_empresa = models.AutoField(verbose_name="Idetendificación Empresa.", primary_key=True)
    nombre_empresa = models.CharField(verbose_name="Nombre Empresa.", null=False, blank=False, max_length=50)
    telefono = models.CharField(verbose_name="Número Telefono.", null=False, blank=False, max_length=50)
    direccion = models.CharField(verbose_name="Dirección.", null=False, blank=False, max_length=50)
    pagina_web = models.URLField(verbose_name="Pagina Web. ")

    def __str__(self):
        return self.nombre_empresa