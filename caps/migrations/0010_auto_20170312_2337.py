# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-12 23:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0009_paciente_terapeutaocupacional'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='assistentesocial',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='avaliacaopsiquiatrica',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='enfermagem',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='entregadedocumentos',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='fisioterapeuta',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='psicologa',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='terapeutaocupacional',
        ),
    ]
