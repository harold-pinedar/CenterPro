# Generated by Django 3.0.4 on 2020-03-31 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sucursal', '0012_auto_20200331_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='regimen',
            field=models.CharField(choices=[('C', 'Común'), ('S', 'Simplificado')], default='C', max_length=2),
        ),
    ]
