# Generated by Django 3.0.4 on 2020-04-01 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordenes_ST', '0018_auto_20200401_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenesst',
            name='estado',
            field=models.CharField(choices=[('E', 'Espera Repuesto'), ('P', 'Pendiente Reparación'), ('D', 'Devolución'), ('R', 'Reparado')], max_length=4, verbose_name='Estado. '),
        ),
    ]
