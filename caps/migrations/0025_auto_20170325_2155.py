# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0024_auto_20170325_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profissional',
            name='quantmaxconsulta',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
