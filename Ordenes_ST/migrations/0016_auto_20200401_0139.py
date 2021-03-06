# Generated by Django 3.0.4 on 2020-04-01 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Colaborador', '0018_auto_20200401_0139'),
        ('Ordenes_ST', '0015_auto_20200401_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenesst',
            name='estado',
            field=models.CharField(choices=[('P', 'Pendiente Reparación'), ('D', 'Devolución'), ('E', 'Espera Repuesto'), ('R', 'Reparado')], max_length=4, verbose_name='Estado. '),
        ),
        migrations.CreateModel(
            name='OrdenEntregadaSt',
            fields=[
                ('id_orden_entregada_st', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('quien_recibe', models.TextField(verbose_name='Nombre de quien recibe.')),
                ('observacion', models.TextField(verbose_name='Observaciones.')),
                ('id_colaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Colaborador.Colaboradores', verbose_name='Nombre de quien entrega.')),
                ('id_orden_st', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Ordenes_ST.OrdenesSt')),
            ],
        ),
    ]
