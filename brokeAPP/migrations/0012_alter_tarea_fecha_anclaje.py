# Generated by Django 5.1.1 on 2024-12-10 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokeAPP', '0011_tarea_cordenadas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fecha_anclaje',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
