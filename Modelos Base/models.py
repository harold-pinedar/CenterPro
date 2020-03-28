# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arl(models.Model):
    id_arl = models.TextField(db_column='ID_ARL', primary_key=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    nombre_emp_arl = models.TextField(db_column='Nombre_Emp_Arl', blank=True, null=True)  # Field name made lowercase.
    fecha_afiliacion = models.DateField(db_column='Fecha_Afiliacion', blank=True, null=True)  # Field name made lowercase.
    fecha_ult_pago = models.DateField(db_column='Fecha_Ult_Pago', blank=True, null=True)  # Field name made lowercase.
    adjunto = models.TextField(db_column='Adjunto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ARL'


class AdelantosSalario(models.Model):
    id_adelantos_salario = models.TextField(db_column='ID_Adelantos_Salario', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    mes = models.TextField(db_column='Mes', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase.
    valor = models.TextField(db_column='Valor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cancelacion_prestamo = models.BooleanField(db_column='Cancelacion_Prestamo', blank=True, null=True)  # Field name made lowercase.
    recibo_adjunto = models.TextField(db_column='Recibo_Adjunto', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Adelantos_Salario'


class AnularSt(models.Model):
    id_anular_st = models.TextField(db_column='ID_Anular_ST', primary_key=True)  # Field name made lowercase.
    id_orden_st = models.TextField(db_column='ID_Orden_ST', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    observacion = models.TextField(db_column='Observacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anular_ST'


class AnularVenta(models.Model):
    id_anular_venta = models.TextField(db_column='ID_Anular_Venta', primary_key=True)  # Field name made lowercase.
    id_venta = models.TextField(db_column='ID_Venta', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    id_cliente = models.TextField(db_column='ID_Cliente', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    motivo = models.TextField(db_column='Motivo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anular_Venta'


class Articulos(models.Model):
    id_articulo = models.TextField(db_column='ID_Articulo', primary_key=True)  # Field name made lowercase.
    id_categoria = models.TextField(db_column='ID_Categoria', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    referencia = models.TextField(db_column='Referencia', blank=True, null=True)  # Field name made lowercase.
    color = models.TextField(db_column='Color', blank=True, null=True)  # Field name made lowercase.
    tamaño = models.TextField(db_column='Tamaño', blank=True, null=True)  # Field name made lowercase.
    valor_un_compra = models.TextField(db_column='Valor_Un_Compra', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    valor_un_venta = models.TextField(db_column='Valor_Un_Venta', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    valor_min_venta = models.TextField(db_column='Valor_Min_Venta', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cantidad_existente = models.DecimalField(db_column='Cantidad_Existente', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    stock_min = models.DecimalField(db_column='Stock_Min', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    stock_max = models.DecimalField(db_column='Stock_Max', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.
    tipo = models.TextField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    remision = models.BooleanField(db_column='Remision', blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(db_column='Foto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Articulos'


class Bancos(models.Model):
    id_banco = models.TextField(db_column='ID_Banco', primary_key=True)  # Field name made lowercase.
    nombre_cuenta = models.TextField(db_column='Nombre_Cuenta', blank=True, null=True)  # Field name made lowercase.
    bancos = models.TextField(db_column='Bancos', blank=True, null=True)  # Field name made lowercase.
    saldo = models.TextField(db_column='Saldo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Bancos'


class Cargos(models.Model):
    id_cargo = models.TextField(db_column='ID_Cargo', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cargos'


class CategoriaArticulo(models.Model):
    id_categoria_articulo = models.TextField(db_column='ID_Categoria_Articulo', primary_key=True)  # Field name made lowercase.
    nombre_categoria = models.TextField(db_column='Nombre_Categoria', blank=True, null=True)  # Field name made lowercase.
    codigo_inicial = models.DecimalField(db_column='Codigo_Inicial', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    codigo_final = models.DecimalField(db_column='Codigo_Final', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categoria_Articulo'


class CategoriaSalida(models.Model):
    id_categoria_salida = models.TextField(db_column='ID_Categoria_Salida', primary_key=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.
    nombre_categoria = models.TextField(db_column='Nombre_Categoria', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categoria_Salida'


class Clientes(models.Model):
    id_cliente = models.TextField(db_column='ID_Cliente', primary_key=True)  # Field name made lowercase.
    identificacion_cliente = models.TextField(db_column='Identificacion_Cliente', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    celular = models.TextField(db_column='Celular', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    fecha_nacimiento = models.DateField(db_column='Fecha_Nacimiento', blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clientes'


class Colaboradores(models.Model):
    id_colaborador = models.TextField(db_column='ID_Colaborador', primary_key=True)  # Field name made lowercase.
    identificacion_colaborador = models.TextField(db_column='Identificacion_Colaborador', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    celular = models.TextField(db_column='Celular', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(db_column='Foto', blank=True, null=True)  # Field name made lowercase.
    rh = models.TextField(db_column='RH', blank=True, null=True)  # Field name made lowercase.
    hoja_de_vida = models.TextField(db_column='Hoja_De_Vida', blank=True, null=True)  # Field name made lowercase.
    fecha_inicio_trabajo = models.DateField(db_column='Fecha_Inicio_Trabajo', blank=True, null=True)  # Field name made lowercase.
    contrato = models.TextField(db_column='Contrato', blank=True, null=True)  # Field name made lowercase.
    id_cargo = models.TextField(db_column='ID_Cargo', blank=True, null=True)  # Field name made lowercase.
    porcentaje_utilidad = models.FloatField(db_column='Porcentaje_Utilidad', blank=True, null=True)  # Field name made lowercase.
    salario = models.TextField(db_column='Salario', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pago_porcentaje = models.FloatField(db_column='Pago_Porcentaje', blank=True, null=True)  # Field name made lowercase.
    maximo_valor_prestamo = models.TextField(db_column='Maximo_Valor_Prestamo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Colaboradores'


class Consultas(models.Model):
    id_consulta = models.TextField(db_column='ID_Consulta', primary_key=True)  # Field name made lowercase.
    id_usuario = models.TextField(db_column='ID_Usuario', blank=True, null=True)  # Field name made lowercase.
    registro_consultado = models.TextField(db_column='Registro_Consultado', blank=True, null=True)  # Field name made lowercase.
    consulta_st = models.TextField(db_column='Consulta_St', blank=True, null=True)  # Field name made lowercase.
    categoria = models.TextField(db_column='Categoria', blank=True, null=True)  # Field name made lowercase.
    consulta_cliente = models.TextField(db_column='Consulta_Cliente', blank=True, null=True)  # Field name made lowercase.
    consulta_producto = models.TextField(db_column='Consulta_Producto', blank=True, null=True)  # Field name made lowercase.
    consulta_repuesto = models.TextField(db_column='Consulta_Repuesto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Consultas'


class ContactoEmpresa(models.Model):
    id_contacto = models.TextField(db_column='ID_Contacto', primary_key=True)  # Field name made lowercase.
    nombre_contacto = models.TextField(db_column='Nombre_Contacto', blank=True, null=True)  # Field name made lowercase.
    telefono_contacto = models.DecimalField(db_column='Telefono_Contacto', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    email_contacto = models.TextField(db_column='Email_Contacto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contacto_Empresa'


class ContactoProveedor(models.Model):
    id_contacto_proveedor = models.TextField(db_column='ID_Contacto_Proveedor', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    telefono = models.TextField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contacto_Proveedor'


class Empresas(models.Model):
    id_empresa = models.TextField(db_column='ID_Empresa', primary_key=True)  # Field name made lowercase.
    nombre_empresa = models.TextField(db_column='Nombre_Empresa', blank=True, null=True)  # Field name made lowercase.
    telefono = models.TextField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    pagina_web = models.TextField(db_column='Pagina_Web', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empresas'


class EncCompra(models.Model):
    id_compra = models.TextField(db_column='ID_Compra', primary_key=True)  # Field name made lowercase.
    id_proveedor = models.TextField(db_column='ID_Proveedor', blank=True, null=True)  # Field name made lowercase.
    fecha_hora_ingreso = models.DateTimeField(db_column='Fecha_Hora_Ingreso', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    descuentos = models.TextField(db_column='Descuentos', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    num_factura = models.TextField(db_column='Num_Factura', blank=True, null=True)  # Field name made lowercase.
    observacion = models.TextField(db_column='Observacion', blank=True, null=True)  # Field name made lowercase.
    adjuntar_factura = models.TextField(db_column='Adjuntar_Factura', blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.
    sub_total_compra = models.TextField(db_column='Sub_Total_Compra', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_impuestos = models.TextField(db_column='Total_Impuestos', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_compra = models.TextField(db_column='Total_Compra', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_remision = models.BooleanField(db_column='En_Remision', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Enc_Compra'


class EncDevVenta(models.Model):
    id_dev_venta = models.TextField(db_column='ID_Dev_Venta', primary_key=True)  # Field name made lowercase.
    id_venta = models.TextField(db_column='ID_Venta', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Enc_Dev_Venta'


class EncNomina(models.Model):
    id_enc_nomina = models.TextField(db_column='ID_Enc_Nomina', primary_key=True)  # Field name made lowercase.
    id_numero_pago = models.DecimalField(db_column='ID_Numero_Pago', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    fecha_hora = models.DateTimeField(db_column='Fecha_Hora', blank=True, null=True)  # Field name made lowercase.
    valor_total = models.TextField(db_column='Valor_Total', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_arl = models.TextField(db_column='Total_ARL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_salud = models.TextField(db_column='Total_Salud', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_nomina = models.TextField(db_column='Total_Nomina', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Enc_Nomina'


class EncPruebasRecepcionSt(models.Model):
    id_pruebas_recepcion_st = models.TextField(db_column='ID_Pruebas_Recepcion_ST', primary_key=True)  # Field name made lowercase.
    id_orden_st = models.TextField(db_column='ID_Orden_ST', blank=True, null=True)  # Field name made lowercase.
    fecha_hora = models.DateTimeField(db_column='Fecha_Hora', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    comentario_general_pruebas = models.TextField(db_column='Comentario_General_Pruebas', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Enc_Pruebas_Recepcion_ST'


class EncSalidaEntradaInventario(models.Model):
    id_enc_salida_entrada_inventario = models.TextField(db_column='ID_Enc_Salida_Entrada_Inventario', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    tipo = models.TextField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Enc_Salida_Entrada_Inventario'


class EncTraspasosArticulo(models.Model):
    id_enc_traspaso = models.TextField(db_column='ID_Enc_Traspaso', primary_key=True)  # Field name made lowercase.
    sucursal_origen = models.TextField(db_column='Sucursal_Origen', blank=True, null=True)  # Field name made lowercase.
    sucursal_destino = models.TextField(db_column='Sucursal_Destino', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Enc_Traspasos_Articulo'


class EncVenta(models.Model):
    id_venta = models.TextField(db_column='ID_Venta', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    id_cliente = models.TextField(db_column='ID_Cliente', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    tipo_pago = models.TextField(db_column='Tipo_Pago', blank=True, null=True)  # Field name made lowercase.
    total_descuentos = models.TextField(db_column='Total_Descuentos', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_venta = models.TextField(db_column='Total_Venta', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    saldo_venta = models.TextField(db_column='Saldo_Venta', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_remision = models.BooleanField(db_column='En_Remision', blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.
    cantidad_px_consulta = models.DecimalField(db_column='Cantidad_Px_Consulta', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    desc_px_consulta = models.TextField(db_column='Desc_Px_Consulta', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    px_consulta = models.TextField(db_column='Px_Consulta', blank=True, null=True)  # Field name made lowercase.
    valor_pagado = models.TextField(db_column='Valor_Pagado', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    usuario = models.TextField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    descuento_total = models.TextField(db_column='Descuento_Total', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Enc_Venta'


class EncaPagosTecnico(models.Model):
    id_pagos_tecnico = models.TextField(db_column='ID_Pagos_Tecnico', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    valor = models.TextField(db_column='Valor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comision = models.FloatField(db_column='Comision', blank=True, null=True)  # Field name made lowercase.
    liquidada = models.BooleanField(db_column='Liquidada', blank=True, null=True)  # Field name made lowercase.
    fecha_inicio_pago = models.DateField(db_column='Fecha_Inicio_Pago', blank=True, null=True)  # Field name made lowercase.
    fecha_final_pago = models.DateField(db_column='Fecha_Final_Pago', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Enca_Pagos_Tecnico'


class Home(models.Model):
    app_name = models.TextField(db_column='App_Name', primary_key=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    app_link = models.TextField(db_column='App_Link', blank=True, null=True)  # Field name made lowercase.
    categoria = models.TextField(db_column='Categoria', blank=True, null=True)  # Field name made lowercase.
    orden = models.DecimalField(db_column='Orden', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Home'


class Marcas(models.Model):
    id_marca = models.TextField(db_column='ID_Marca', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    id_tipo_equipo = models.TextField(db_column='ID_Tipo_Equipo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Marcas'


class Modelos(models.Model):
    id_modelo = models.TextField(db_column='ID_Modelo', primary_key=True)  # Field name made lowercase.
    id_marca = models.TextField(db_column='ID_Marca', blank=True, null=True)  # Field name made lowercase.
    modelo = models.TextField(db_column='Modelo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Modelos'


class MovCompra(models.Model):
    id_mov_compra = models.TextField(db_column='ID_Mov_Compra', primary_key=True)  # Field name made lowercase.
    id_compra = models.TextField(db_column='ID_Compra', blank=True, null=True)  # Field name made lowercase.
    id_articulo = models.TextField(db_column='ID_Articulo', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    valor_un = models.TextField(db_column='Valor_Un', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sub_total = models.TextField(db_column='Sub_Total', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    descuento = models.TextField(db_column='Descuento', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mov_Compra'


class MovDevVenta(models.Model):
    id_mov_dev_venta = models.TextField(db_column='ID_Mov_Dev_Venta', primary_key=True)  # Field name made lowercase.
    id_dev_venta = models.TextField(db_column='ID_Dev_Venta', blank=True, null=True)  # Field name made lowercase.
    id_articulo = models.TextField(db_column='ID_Articulo', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    observacion = models.TextField(db_column='Observacion', blank=True, null=True)  # Field name made lowercase.
    valor_unitario = models.TextField(db_column='Valor_Unitario', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    descuento = models.TextField(db_column='Descuento', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Mov_Dev_Venta'


class MovPagoNomina(models.Model):
    id_pago = models.TextField(db_column='ID_Pago', primary_key=True)  # Field name made lowercase.
    numero_pago = models.DecimalField(db_column='Numero_Pago', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    adelantos = models.TextField(db_column='Adelantos', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    descuentos = models.TextField(db_column='Descuentos', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_arl = models.TextField(db_column='ID_ARL', blank=True, null=True)  # Field name made lowercase.
    id_seg_social = models.TextField(db_column='ID_Seg_Social', blank=True, null=True)  # Field name made lowercase.
    pension = models.TextField(db_column='Pension', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    transporte = models.TextField(db_column='Transporte', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    field_horas_extras_diurnas = models.DecimalField(db_column='#_Horas_Extras_Diurnas', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_horas_extras_nocturnas = models.DecimalField(db_column='#_Horas_Extras_Nocturnas', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_hora_extras_festivos = models.DecimalField(db_column='#-Hora_Extras_Festivos', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    neto_pago = models.TextField(db_column='Neto_Pago', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    observacion = models.TextField(db_column='Observacion', blank=True, null=True)  # Field name made lowercase.
    total_porcentaje = models.FloatField(db_column='Total_Porcentaje', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mov_Pago_Nomina'


class MovSalidaEntradaInventario(models.Model):
    id_mov_salida_entrada_inventario = models.TextField(db_column='ID_Mov_Salida_Entrada_Inventario', primary_key=True)  # Field name made lowercase.
    id_enc_salida_entrada_inventario = models.TextField(db_column='ID_Enc_Salida_Entrada_Inventario', blank=True, null=True)  # Field name made lowercase.
    id_articulo = models.TextField(db_column='ID_Articulo', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    costo = models.TextField(db_column='Costo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mov_Salida_Entrada_Inventario'


class MovVenta(models.Model):
    id_mov_venta = models.TextField(db_column='ID_Mov_Venta', primary_key=True)  # Field name made lowercase.
    id_venta = models.TextField(db_column='ID_Venta', blank=True, null=True)  # Field name made lowercase.
    id_articulo = models.TextField(db_column='ID_Articulo', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    valor_unitario = models.TextField(db_column='Valor_Unitario', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    descuento = models.TextField(db_column='Descuento', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    subtotal = models.TextField(db_column='Subtotal', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mov_Venta'


class MvtoPagosTecnico(models.Model):
    id_mto_pago_tecnico = models.TextField(db_column='ID_Mto_Pago_Tecnico', primary_key=True)  # Field name made lowercase.
    id_pagos_tecnico = models.TextField(db_column='ID_Pagos_Tecnico', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    id_orden_st = models.TextField(db_column='ID_Orden_ST', blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.FloatField(db_column='Porcentaje', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mvto_Pagos_Tecnico'


class MvtoPruebasRecepcion(models.Model):
    id_mvto_pruebas_recepcion = models.TextField(db_column='ID_Mvto_Pruebas_Recepcion', primary_key=True)  # Field name made lowercase.
    id_pruebas_recepcion_st = models.TextField(db_column='ID_Pruebas_Recepcion_ST', blank=True, null=True)  # Field name made lowercase.
    id_prueba = models.TextField(db_column='ID_Prueba', blank=True, null=True)  # Field name made lowercase.
    descripcion_estado = models.TextField(db_column='Descripcion_Estado', blank=True, null=True)  # Field name made lowercase.
    resultado_prueba = models.BooleanField(db_column='Resultado_Prueba', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mvto_Pruebas_Recepcion'


class MvtoTraspasoArticulo(models.Model):
    id_mto_traspaso = models.TextField(db_column='ID_Mto_Traspaso', primary_key=True)  # Field name made lowercase.
    id_articulo = models.TextField(db_column='ID_Articulo', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    costo_unitario = models.TextField(db_column='Costo_Unitario', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    subtotal = models.TextField(db_column='Subtotal', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mvto_Traspaso_Articulo'


class OrdenDevolucionSt(models.Model):
    id_orden_devolucion_st = models.TextField(db_column='ID_Orden_Devolucion_ST', primary_key=True)  # Field name made lowercase.
    id_orden_st = models.TextField(db_column='ID_Orden_ST', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    concepto_devolucion = models.TextField(db_column='Concepto_Devolucion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orden_Devolucion_ST'


class OrdenEntregadaSt(models.Model):
    id_orden_entregada_st = models.TextField(db_column='ID_Orden_Entregada_ST', primary_key=True)  # Field name made lowercase.
    id_orden_st = models.TextField(db_column='ID_Orden_ST', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    quien_recibe = models.TextField(db_column='Quien_Recibe', blank=True, null=True)  # Field name made lowercase.
    observacion = models.TextField(db_column='Observacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orden_Entregada_ST'


class OrdenEsperaRepSt(models.Model):
    id_orden_espera_rep_st = models.TextField(db_column='ID_Orden_Espera_Rep_ST', primary_key=True)  # Field name made lowercase.
    id_orden_st = models.TextField(db_column='ID_Orden_ST', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    motivo_espera = models.TextField(db_column='Motivo_Espera', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orden_Espera_Rep_ST'


class OrdenReparadaSt(models.Model):
    id_orden_reparada_st = models.TextField(db_column='ID_Orden_Reparada_ST', primary_key=True)  # Field name made lowercase.
    id_orden_st = models.TextField(db_column='ID_Orden_ST', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    precio = models.TextField(db_column='Precio', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    solucion = models.TextField(db_column='Solucion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orden_Reparada_ST'


class OrdenesSt(models.Model):
    id_orden_st = models.TextField(db_column='ID_Orden_ST', primary_key=True)  # Field name made lowercase.
    orden_st = models.DecimalField(db_column='Orden_ST', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    cliente_documento = models.TextField(db_column='Cliente_Documento', blank=True, null=True)  # Field name made lowercase.
    notificar_otro_no = models.TextField(db_column='Notificar_Otro_No', blank=True, null=True)  # Field name made lowercase.
    id_tipo_equipo = models.TextField(db_column='ID_Tipo_Equipo', blank=True, null=True)  # Field name made lowercase.
    id_marca = models.TextField(db_column='ID_Marca', blank=True, null=True)  # Field name made lowercase.
    id_modelo = models.TextField(db_column='ID_Modelo', blank=True, null=True)  # Field name made lowercase.
    equipo_serial = models.DecimalField(db_column='Equipo_Serial', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    equipo_serial2 = models.DecimalField(db_column='Equipo_Serial2', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    verificacion_imei = models.TextField(db_column='Verificacion_IMEI', blank=True, null=True)  # Field name made lowercase.
    verificacion_imei2 = models.TextField(db_column='Verificacion_IMEI2', blank=True, null=True)  # Field name made lowercase.
    contrasena = models.TextField(db_column='Contrasena', blank=True, null=True)  # Field name made lowercase.
    patron = models.TextField(db_column='Patron', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    fecha_posible = models.DateField(db_column='Fecha_Posible', blank=True, null=True)  # Field name made lowercase.
    registro_fecha = models.DateField(db_column='Registro_Fecha', blank=True, null=True)  # Field name made lowercase.
    registro_hora = models.TimeField(db_column='Registro_Hora', blank=True, null=True)  # Field name made lowercase.
    fecha_entrega = models.DateField(db_column='Fecha_Entrega', blank=True, null=True)  # Field name made lowercase.
    motivo_entrada = models.TextField(db_column='Motivo_Entrada', blank=True, null=True)  # Field name made lowercase.
    valor = models.TextField(db_column='Valor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.
    garantia = models.TextField(db_column='Garantia', blank=True, null=True)  # Field name made lowercase.
    id_tecnico = models.TextField(db_column='ID_Tecnico', blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(db_column='Foto', blank=True, null=True)  # Field name made lowercase.
    switch_con_patron = models.TextField(db_column='Switch_Con_patron', blank=True, null=True)  # Field name made lowercase.
    abono_inicial = models.TextField(db_column='Abono_Inicial', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Ordenes_ST'


class PagosAbonosCompras(models.Model):
    id_pagos_abonos_compras = models.TextField(db_column='ID_Pagos_Abonos_Compras', primary_key=True)  # Field name made lowercase.
    id_compra = models.TextField(db_column='ID_Compra', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    tipo_pago = models.BooleanField(db_column='Tipo_Pago', blank=True, null=True)  # Field name made lowercase.
    forma_pago = models.TextField(db_column='Forma_Pago', blank=True, null=True)  # Field name made lowercase.
    saldo_anterior = models.TextField(db_column='Saldo_Anterior', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    valor = models.TextField(db_column='Valor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    saldo = models.TextField(db_column='Saldo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_banco = models.TextField(db_column='ID_Banco', blank=True, null=True)  # Field name made lowercase.
    numero_pago = models.TextField(db_column='Numero_Pago', blank=True, null=True)  # Field name made lowercase.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase.
    foto_comprobante = models.TextField(db_column='Foto_Comprobante', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pagos_Abonos_Compras'


class PagosSt(models.Model):
    id_pago = models.TextField(db_column='ID_Pago', primary_key=True)  # Field name made lowercase.
    id_orden_st = models.TextField(db_column='ID_Orden_ST', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    saldo_inicial = models.TextField(db_column='Saldo_Inicial', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    valor = models.TextField(db_column='Valor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    forma_pago = models.BooleanField(db_column='Forma_Pago', blank=True, null=True)  # Field name made lowercase.
    abono_pago = models.TextField(db_column='Abono_Pago', blank=True, null=True)  # Field name made lowercase.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.
    saldo_final = models.TextField(db_column='Saldo_Final', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Pagos_ST'


class PagosVentas(models.Model):
    id_pago_venta = models.TextField(db_column='ID_Pago_Venta', primary_key=True)  # Field name made lowercase.
    id_venta = models.TextField(db_column='ID_Venta', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    saldo_inicial = models.TextField(db_column='Saldo_Inicial', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tipo_pago = models.BooleanField(db_column='Tipo_Pago', blank=True, null=True)  # Field name made lowercase.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.
    saldo_final = models.TextField(db_column='Saldo_Final', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    valor = models.TextField(db_column='Valor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_banco = models.TextField(db_column='ID_Banco', blank=True, null=True)  # Field name made lowercase.
    referencia_banco = models.TextField(db_column='Referencia_Banco', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pagos_Ventas'


class ProveedorArticulo(models.Model):
    id = models.TextField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_proveedor = models.TextField(db_column='ID_Proveedor', blank=True, null=True)  # Field name made lowercase.
    id_articulo = models.TextField(db_column='ID_Articulo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proveedor_Articulo'


class Proveedores(models.Model):
    id_proveedor = models.TextField(db_column='ID_Proveedor', primary_key=True)  # Field name made lowercase.
    identificacion_proveedor = models.TextField(db_column='Identificacion_Proveedor', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    celular = models.TextField(db_column='Celular', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    ciudad = models.TextField(db_column='Ciudad', blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proveedores'


class Pruebas(models.Model):
    id_prueba = models.TextField(db_column='ID_Prueba', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pruebas'


class ReferenciasColaborador(models.Model):
    id_referencia = models.TextField(db_column='ID_Referencia', primary_key=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    identidicacion = models.TextField(db_column='Identidicacion', blank=True, null=True)  # Field name made lowercase.
    celular = models.TextField(db_column='Celular', blank=True, null=True)  # Field name made lowercase.
    cargo = models.TextField(db_column='Cargo', blank=True, null=True)  # Field name made lowercase.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Referencias_Colaborador'


class RepuestosInsumosConsumidos(models.Model):
    id_rep_ins_con = models.TextField(db_column='ID_Rep_Ins_con', primary_key=True)  # Field name made lowercase.
    id_orden_st = models.TextField(db_column='ID_Orden_ST', blank=True, null=True)  # Field name made lowercase.
    id_articulo = models.TextField(db_column='ID_Articulo', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    costo = models.TextField(db_column='Costo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comentarios = models.TextField(db_column='Comentarios', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    flete = models.TextField(db_column='Flete', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Repuestos_Insumos_Consumidos'


class Roles(models.Model):
    id_rol = models.TextField(db_column='ID_Rol', primary_key=True)  # Field name made lowercase.
    nombre_rol = models.TextField(db_column='Nombre_Rol', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    permisos = models.TextField(db_column='Permisos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Roles'


class Salidas(models.Model):
    id_gasto = models.TextField(db_column='ID_Gasto', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    id_proveedor = models.TextField(db_column='ID_Proveedor', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    valor = models.TextField(db_column='Valor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_categoria_salida = models.TextField(db_column='ID_Categoria_Salida', blank=True, null=True)  # Field name made lowercase.
    forma_pago = models.BooleanField(db_column='Forma_Pago', blank=True, null=True)  # Field name made lowercase.
    caja_sucursal = models.BooleanField(db_column='Caja_Sucursal', blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(db_column='Foto', blank=True, null=True)  # Field name made lowercase.
    id_banco = models.TextField(db_column='ID_Banco', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Salidas'


class SegSocial(models.Model):
    id_seg_social = models.TextField(db_column='ID_Seg_Social', primary_key=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    nombre_emp_ss = models.TextField(db_column='Nombre_Emp_SS', blank=True, null=True)  # Field name made lowercase.
    fecha_afiliacion = models.DateField(db_column='Fecha_Afiliacion', blank=True, null=True)  # Field name made lowercase.
    fecha_ult_pago = models.DateField(db_column='Fecha_Ult_Pago', blank=True, null=True)  # Field name made lowercase.
    adjunto = models.TextField(db_column='Adjunto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Seg_Social'


class SubMenu(models.Model):
    id_sub_menu = models.TextField(db_column='ID_Sub_Menu', primary_key=True)  # Field name made lowercase.
    app_name = models.TextField(db_column='App_Name', blank=True, null=True)  # Field name made lowercase.
    app_image = models.TextField(db_column='App_Image', blank=True, null=True)  # Field name made lowercase.
    app_url = models.TextField(db_column='App_Url', blank=True, null=True)  # Field name made lowercase.
    categoria = models.TextField(db_column='Categoria', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sub_Menu'


class Sucursales(models.Model):
    id_sucursal = models.TextField(db_column='ID_Sucursal', primary_key=True)  # Field name made lowercase.
    id_empresa = models.TextField(db_column='ID_Empresa', blank=True, null=True)  # Field name made lowercase.
    nombre_sucursal = models.TextField(db_column='Nombre_Sucursal', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    coordenadas = models.TextField(db_column='Coordenadas', blank=True, null=True)  # Field name made lowercase.
    telefono = models.DecimalField(db_column='Telefono', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    logo = models.TextField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    regimen = models.TextField(db_column='Regimen', blank=True, null=True)  # Field name made lowercase.
    texto_ley_st = models.TextField(db_column='Texto_Ley_ST', blank=True, null=True)  # Field name made lowercase.
    texto_ley_ventas = models.TextField(db_column='Texto_Ley_Ventas', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sucursales'


class TipoEquipo(models.Model):
    id_tipo_equipo = models.TextField(db_column='ID_Tipo_Equipo', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Equipo'


class UsuariosDelSistema(models.Model):
    id_usuario = models.TextField(db_column='ID_Usuario', primary_key=True)  # Field name made lowercase.
    id_colaborador = models.TextField(db_column='ID_Colaborador', blank=True, null=True)  # Field name made lowercase.
    rol = models.TextField(db_column='Rol', blank=True, null=True)  # Field name made lowercase.
    id_sucursal = models.TextField(db_column='ID_Sucursal', blank=True, null=True)  # Field name made lowercase.
    fecha_inicial = models.DateField(db_column='Fecha_Inicial', blank=True, null=True)  # Field name made lowercase.
    fecha_final = models.DateField(db_column='Fecha_Final', blank=True, null=True)  # Field name made lowercase.
    clave = models.TextField(db_column='Clave', blank=True, null=True)  # Field name made lowercase.
    repetir_clave = models.TextField(db_column='Repetir_Clave', blank=True, null=True)  # Field name made lowercase.
    tecnico_consulta = models.TextField(db_column='Tecnico_Consulta', blank=True, null=True)  # Field name made lowercase.
    variable_temp = models.TextField(db_column='Variable_Temp', blank=True, null=True)  # Field name made lowercase.
    cuenta_consulta = models.TextField(db_column='Cuenta_Consulta', blank=True, null=True)  # Field name made lowercase.
    proveedor_consulta = models.TextField(db_column='Proveedor_Consulta', blank=True, null=True)  # Field name made lowercase.
    consulta_menu = models.TextField(db_column='Consulta_Menu', blank=True, null=True)  # Field name made lowercase.
    id_venta = models.TextField(db_column='ID_Venta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuarios_Del_Sistema'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class UsuariosUsuario(models.Model):
    nombre = models.CharField(max_length=55)
    cedula = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios_usuario'
