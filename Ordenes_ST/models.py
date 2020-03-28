from django.db import models
from Colaborador.models import Colaboradores
from Cliente.models import Cliente
from Equipos.models import Marcas, Modelos, TipoEquipo
from Empresa.models import Empresas
from Sucursal.models import Sucursal

# Create your models here.

class OrdenesSt(models.Model):
    id_orden_st = models.BigAutoField(primary_key=True)
    id_colaborador = models.ForeignKey(Colaboradores, null=True, on_delete=models.SET_NULL)
    cliente_documento = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL )
    notificar_otro_no = models.CharField(max_length=10, help_text="Numero Alterno")

    # TIPO_EQUIPOS = {
    #     (" ","CELULARES"), (" ","COMPUTADORES"), ("","TABLE´S"), (" ","PARLANTES"), (" ","OTRO")
    #     } ##PENDIENTE POR PROBAR SI FUNCIONA

    tipo_equipo = models.ForeignKey(TipoEquipo, verbose_name="Tipo De Equipo.", null=True, on_delete=models.SET_NULL)
    id_marca = models.ForeignKey(Marcas, null=True, on_delete=models.SET_NULL)
    id_modelo = models.ForeignKey(Modelos, null=True, on_delete=models.SET_NULL)
    equipo_serial = models.CharField(verbose_name="Imei 1", max_length=15)
    equipo_serial2 = models.CharField(verbose_name="Imei 2", max_length=15)
    verificacion_imei = models.CharField(verbose_name="Imei 1", max_length=15)
    verificacion_imei2 = models.CharField(verbose_name="Imei 2", max_length=15)
    contrasena = models.CharField(verbose_name="Contraseña", max_length=20)
    patron = models.CharField(verbose_name="Patron Desbloque", max_length=20)
    ESTADOS = {
        ("R", "Reparado"), ("D", "Devolución"), ("E", "Espera Repuesto"), ("P", "Pendiente Reparación")
    }
    estado = models.CharField(verbose_name="Estado. ", max_length=4, choices=ESTADOS)
    fecha_posible = models.DateField()
    registro_fecha = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateField()
    motivo_entrada = models.TextField(verbose_name="Motivo De Entrada.")
    valor = models.DecimalField(verbose_name="Valor. ", max_digits=7, decimal_places=2)
    id_empresa = models.ForeignKey(Empresas, null=True, on_delete=models.SET_NULL)
    id_sucursal = models.ForeignKey(Sucursal, null=True, on_delete=models.SET_NULL)
    garantia = models.BooleanField(default=False)
    id_tecnico = models.CharField(max_length=20)
    foto = models.ImageField()
    switch_con_patron = models.CharField(max_length=10)
    abono_inicial = models.DecimalField(verbose_name="Abono.", max_digits=6, decimal_places=2)


    def __str__(self):
        return self.cliente_documento
