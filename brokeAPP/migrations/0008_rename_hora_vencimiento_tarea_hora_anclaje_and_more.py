# Generated by Django 5.1.1 on 2024-12-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokeAPP', '0007_remove_tarea_fecha_asignacion_tarea_fecha_anclaje_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='hora_vencimiento',
            new_name='hora_anclaje',
        ),
        migrations.AddField(
            model_name='tarea',
            name='hora_venconfig',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
