# Generated by Django 3.0.4 on 2020-03-24 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordenes_ST', '0002_auto_20200323_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenesst',
            name='estado',
            field=models.CharField(choices=[('E', 'Espera Repuesto'), ('R', 'Reparado'), ('P', 'Pendiente Reparación'), ('D', 'Devolución')], max_length=4, verbose_name='Estado. '),
        ),
    ]
