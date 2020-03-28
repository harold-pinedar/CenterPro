# Generated by Django 3.0.4 on 2020-03-24 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Colaborador', '0002_auto_20200323_2124'),
        ('Empresa', '0001_initial'),
        ('Cliente', '0003_auto_20200323_1034'),
        ('Sucursal', '0006_auto_20200323_2124'),
        ('Equipos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenesSt',
            fields=[
                ('id_orden_st', models.BigAutoField(primary_key=True, serialize=False)),
                ('notificar_otro_no', models.CharField(help_text='Numero Alterno', max_length=10)),
                ('tipo_equipo', models.CharField(choices=[(' ', 'COMPUTADORES'), ('', 'TABLE´S'), (' ', 'PARLANTES'), (' ', 'OTRO'), (' ', 'CELULARES')], max_length=5, verbose_name='Tipo De Equipo.')),
                ('equipo_serial', models.CharField(max_length=15, verbose_name='Imei 1')),
                ('equipo_serial2', models.CharField(max_length=15, verbose_name='Imei 2')),
                ('verificacion_imei', models.CharField(max_length=15, verbose_name='Imei 1')),
                ('verificacion_imei2', models.CharField(max_length=15, verbose_name='Imei 2')),
                ('contrasena', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('patron', models.CharField(max_length=20, verbose_name='Patron Desbloque')),
                ('estado', models.CharField(choices=[('E', 'Espera Repuesto'), ('R', 'Reparado'), ('P', 'Pendiente Reparación'), ('D', 'Devolución')], max_length=4, verbose_name='Estado. ')),
                ('fecha_posible', models.DateField()),
                ('registro_fecha', models.DateTimeField(auto_now_add=True)),
                ('fecha_entrega', models.DateField()),
                ('motivo_entrada', models.TextField(verbose_name='Motivo De Entrada.')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor. ')),
                ('garantia', models.BooleanField(default=False)),
                ('id_tecnico', models.CharField(max_length=20)),
                ('foto', models.ImageField(upload_to='')),
                ('switch_con_patron', models.CharField(max_length=10)),
                ('abono_inicial', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Abono.')),
                ('cliente_documento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Cliente.Cliente')),
                ('id_colaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Colaborador.Colaboradores')),
                ('id_empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Empresa.Empresas')),
                ('id_marca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Equipos.Marcas')),
                ('id_modelo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Equipos.Modelos')),
                ('id_sucursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sucursal.Sucursal')),
            ],
        ),
    ]
