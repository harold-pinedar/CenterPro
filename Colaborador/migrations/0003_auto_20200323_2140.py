# Generated by Django 3.0.4 on 2020-03-24 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Colaborador', '0002_auto_20200323_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradores',
            name='rh',
            field=models.CharField(choices=[('RH', 'AB+'), ('RH', 'O-'), ('RH', 'B+'), ('RH', 'A+'), ('RH', 'A-'), ('RH', 'O+'), ('RH', 'AB-'), ('RH', 'B-')], max_length=8),
        ),
    ]
