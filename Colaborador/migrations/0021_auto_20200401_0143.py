# Generated by Django 3.0.4 on 2020-04-01 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Colaborador', '0020_auto_20200401_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradores',
            name='rh',
            field=models.CharField(choices=[('RH', 'A+'), ('RH', 'AB+'), ('RH', 'B-'), ('RH', 'O-'), ('RH', 'O+'), ('RH', 'B+'), ('RH', 'AB-'), ('RH', 'A-')], max_length=8),
        ),
    ]
