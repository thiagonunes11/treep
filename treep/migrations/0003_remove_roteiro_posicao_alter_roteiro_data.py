# Generated by Django 4.2.1 on 2023-10-12 00:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('treep', '0002_roteiro_posicao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roteiro',
            name='posicao',
        ),
        migrations.AlterField(
            model_name='roteiro',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
