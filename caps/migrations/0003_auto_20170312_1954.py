# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-12 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0002_auto_20170312_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fone', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='paciente',
            name='rgorgemissor',
            field=models.CharField(choices=[('SSP', 'Secretaria de Segurança Pública'), ('PM', 'Polícia Militar'), ('PC', 'Policia Civil'), ('CNT', 'Carteira Nacional de Habilitação'), ('DIC', 'Diretoria de Identificação Civil'), ('CTPS', 'Carteira de Trabaho e Previdência Social'), ('FGTS', 'Fundo de Garantia do Tempo de Serviço'), ('IFP', 'Instituto Félix Pacheco'), ('IPF', 'Instituto Pereira Faustino'), ('IML', 'Instituto Médico-Legal'), ('MTE', 'Ministério do Trabalho e Emprego'), ('MMA', 'Ministério da Marinha'), ('MAE', 'Ministério da Aeronáutica'), ('MEX', 'Ministério do Exército'), ('POF', 'Polícia Federal'), ('POM', 'Polícia Militar'), ('SES', 'Carteira de Estrangeiro'), ('SJS', 'Secretaria da Justiça e Segurança'), ('SJTS', 'Secretaria da Justiça do Trabalho e Segurança'), ('ZZZ', 'Outros (inclusive exterior')], max_length=255),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='rguf',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2),
        ),
    ]
