# Generated by Django 3.0.4 on 2020-04-01 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sucursal', '0018_auto_20200401_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='regimen',
            field=models.CharField(choices=[('C', 'Común'), ('S', 'Simplificado')], default='C', max_length=2),
        ),
    ]
