# Generated by Django 2.2.7 on 2019-11-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
