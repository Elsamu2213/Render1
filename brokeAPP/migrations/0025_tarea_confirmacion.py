# Generated by Django 5.1.1 on 2025-01-06 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokeAPP', '0024_remove_salario_fecha_pago_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='confirmacion',
            field=models.BooleanField(default=False),
        ),
    ]
