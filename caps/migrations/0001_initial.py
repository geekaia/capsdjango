# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('numsus', models.IntegerField()),
                ('endereco', models.CharField(max_length=255)),
                ('pontoreferencia', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=255)),
                ('fone', models.CharField(max_length=14)),
                ('certidao', models.CharField(choices=[('nasc', 'Nascimento'), ('casa', 'Casamento'), ('divo', 'Divórcio')], max_length=3)),
                ('livro', models.CharField(max_length=100)),
                ('fls', models.CharField(max_length=100)),
                ('termo', models.CharField(max_length=100)),
                ('dataemissao', models.DateField()),
                ('datanascimento', models.DateField()),
                ('rg', models.CharField(max_length=50)),
                ('rgorgemissor', models.CharField(max_length=255)),
                ('rguf', models.CharField(max_length=2)),
                ('rgdataemissao', models.DateField()),
                ('cpf', models.CharField(max_length=15)),
                ('apelido', models.CharField(max_length=255)),
                ('nomepai', models.CharField(max_length=255)),
                ('nomemae', models.CharField(max_length=255)),
                ('nomeresponsavel', models.CharField(max_length=255)),
                ('festratamento', models.CharField(max_length=255)),
                ('encaminhadopor', models.CharField(max_length=255)),
            ],
        ),
    ]
