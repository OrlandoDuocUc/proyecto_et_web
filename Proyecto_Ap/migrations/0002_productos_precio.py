# Generated by Django 5.0.6 on 2024-06-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Ap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='precio',
            field=models.IntegerField(default=1000, verbose_name='Precio'),
        ),
    ]
