# Generated by Django 3.0.4 on 2020-04-01 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sucursal', '0017_auto_20200401_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='regimen',
            field=models.CharField(choices=[('S', 'Simplificado'), ('C', 'Común')], default='C', max_length=2),
        ),
    ]
