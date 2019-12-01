# Generated by Django 2.2.6 on 2019-11-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Muelitas', '0006_auto_20191115_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial_clinico',
            name='RH',
            field=models.TextField(choices=[('0', 'RH'), ('1', 'A+'), ('2', 'A-'), ('3', 'B+'), ('4', 'B-'), ('5', 'AB+'), ('6', 'AB-'), ('7', 'O+'), ('8', 'O-')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='historial_clinico',
            name='estadoCivil',
            field=models.TextField(choices=[('0', 'estado civil'), ('1', 'soltero'), ('2', 'comprometido/a'), ('3', 'casado'), ('4', 'union libre'), ('5', 'divorciado/a'), ('6', 'viudo/a')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='historial_clinico',
            name='sexo',
            field=models.CharField(choices=[('0', 'sexo'), ('1', 'Femenino'), ('2', 'Masculino')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('2', 'odontologo'), ('1', 'secretaria'), ('3', 'paciente')], default='3', max_length=1),
        ),
    ]
