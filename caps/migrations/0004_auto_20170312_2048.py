# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-12 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0003_auto_20170312_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='encaminhadopor',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='festratamento',
            field=models.CharField(choices=[('NAO', 'NÃO'), ('SIM', 'SIM')], max_length=255),
        ),
    ]
