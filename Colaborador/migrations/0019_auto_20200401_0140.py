# Generated by Django 3.0.4 on 2020-04-01 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Colaborador', '0018_auto_20200401_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradores',
            name='rh',
            field=models.CharField(choices=[('RH', 'AB+'), ('RH', 'B+'), ('RH', 'O-'), ('RH', 'A+'), ('RH', 'A-'), ('RH', 'O+'), ('RH', 'AB-'), ('RH', 'B-')], max_length=8),
        ),
    ]
