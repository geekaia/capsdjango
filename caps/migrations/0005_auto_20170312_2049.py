# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-12 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0004_auto_20170312_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='encaminhadopor',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
