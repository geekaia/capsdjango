# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0014_auto_20170320_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='email',
            field=models.CharField(blank=True, default='', max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tipoendereco',
            field=models.CharField(blank=True, choices=[('Aeroporto', 'Aeroporto'), ('Alameda', 'Alameda'), ('Área', 'Área'), ('Avenida', 'Avenida'), ('Campo', 'Campo'), ('Chácara', 'Chácara'), ('Colônia', 'Colônia'), ('Condomínio', 'Condomínio'), ('Conjunto', 'Conjunto'), ('Distrito', 'Distrito'), ('Esplanada', 'Esplanada'), ('Estação', 'Estação'), ('Estrada', 'Estrada'), ('Favela', 'Favela'), ('Fazenda', 'Fazenda'), ('Feira', 'Feira'), ('Jardim', 'Jardim'), ('Ladeira', 'Ladeira'), ('Lago', 'Lago'), ('Lagoa', 'Lagoa'), ('Largo', 'Largo'), ('Loteamento', 'Loteamento'), ('Morro', 'Morro'), ('Núcleo', 'Núcleo'), ('Parque', 'Parque'), ('Passarela', 'Passarela'), ('Pátio', 'Pátio'), ('Praça', 'Praça'), ('Quadra', 'Quadra'), ('Recanto', 'Recanto'), ('Residencial', 'Residencial'), ('Rodovia', 'Rodovia'), ('Rua', 'Rua'), ('Setor', 'Setor'), ('Sítio', 'Sítio'), ('Travessa', 'Travessa'), ('Trecho', 'Trecho'), ('Trevo', 'Trevo'), ('Vale', 'Vale'), ('Vereda', 'Vereda'), ('Via', 'Via'), ('Viaduto', 'Viaduto'), ('Viela', 'Viela'), ('Vila', 'Vila')], default='', max_length=30, null=True),
        ),
    ]
