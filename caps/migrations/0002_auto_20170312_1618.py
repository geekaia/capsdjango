# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='certidao',
            field=models.CharField(choices=[('nas', 'Nascimento'), ('cas', 'Casamento'), ('div', 'Divórcio')], max_length=3),
        ),
    ]
