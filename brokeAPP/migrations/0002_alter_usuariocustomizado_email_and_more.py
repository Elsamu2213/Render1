# Generated by Django 5.1.1 on 2024-10-18 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokeAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariocustomizado',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usuariocustomizado',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
