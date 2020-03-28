from django.db import models

# Create your models here.


class Colaboradores(models.Model):
    identificacion_colaborador = models.CharField(verbose_name="Identificación",  max_length=20, primary_key=True)  
    nombre = models.CharField(verbose_name="Nombre. ", max_length=70)
    celular = models.CharField(verbose_name="Número Celular. ", max_length=10, null=False, blank=False)
    email = models.EmailField()
    direccion = models.CharField(verbose_name="Direccion.", max_length=255)  
    foto = models.ImageField()  
    RH = {
        ("RH","AB+"), ("RH","AB-"), ("RH","A+"), ("RH","A-"), ("RH","B+"), ("RH","B-"), ("RH","O+"), ("RH","O-"),
        }
    rh = models.CharField(max_length=8, choices=RH)
    hoja_de_vida = models.FileField(upload_to="") 
    fecha_inicio_trabajo = models.DateField()
    contrato = models.CharField(max_length=2) #Tipo De Contrato
    id_cargo = models.CharField(max_length=2) #Pendiente por traer Table
    porcentaje_utilidad = models.DecimalField(verbose_name="Porcentaje Utilidad ", max_digits=6, decimal_places=2)
    salario = models.DecimalField(verbose_name="Salario",max_digits=6, decimal_places=2)
    pago_porcentaje = models.DecimalField(verbose_name="Pago Porcentaje",max_digits=6, decimal_places=2)
    maximo_valor_prestamo = models.DecimalField(verbose_name="Maximo Valor Prestado",max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre
