# Generated by Django 3.0.4 on 2020-03-31 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Colaborador', '0010_auto_20200331_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradores',
            name='rh',
            field=models.CharField(choices=[('RH', 'A+'), ('RH', 'AB+'), ('RH', 'B+'), ('RH', 'O+'), ('RH', 'AB-'), ('RH', 'O-'), ('RH', 'A-'), ('RH', 'B-')], max_length=8),
        ),
    ]
