# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 22:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0020_auto_20170321_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='validadefim',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='horario',
            name='validadeinicio',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
