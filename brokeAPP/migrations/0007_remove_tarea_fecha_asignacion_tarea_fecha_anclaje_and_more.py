# Generated by Django 5.1.1 on 2024-12-10 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokeAPP', '0006_tareaavanzada_tarea_cod_postal_tarea_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='fecha_asignacion',
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_anclaje',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarea',
            name='hora_vencimiento',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
