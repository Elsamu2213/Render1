# Generated by Django 5.1.1 on 2024-12-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokeAPP', '0008_rename_hora_vencimiento_tarea_hora_anclaje_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fecha_anclaje',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_vencimiento',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='hora_anclaje',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='hora_venconfig',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
