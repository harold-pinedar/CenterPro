# Generated by Django 3.0.4 on 2020-03-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sucursal', '0009_auto_20200329_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='regimen',
            field=models.CharField(choices=[('S', 'Simplificado'), ('C', 'Común')], default='C', max_length=2),
        ),
    ]
