# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0017_auto_20170321_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='numsus',
            field=models.CharField(max_length=255),
        ),
    ]
