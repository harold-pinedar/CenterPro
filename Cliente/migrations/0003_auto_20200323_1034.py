# Generated by Django 3.0.4 on 2020-03-23 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sucursal', '0003_auto_20200323_1034'),
        ('Cliente', '0002_auto_20200323_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='disabled',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='id_sucursal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Sucursal.Sucursal'),
        ),
    ]
