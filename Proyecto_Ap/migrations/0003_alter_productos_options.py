# Generated by Django 5.0.6 on 2024-06-30 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto_Ap', '0002_productos_precio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productos',
            options={'permissions': (('editar_producto', 'Editar productos'),)},
        ),
    ]
