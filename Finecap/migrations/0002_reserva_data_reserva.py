# Generated by Django 4.2.5 on 2023-09-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finecap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateField(blank=True, null=True),
        ),
    ]
