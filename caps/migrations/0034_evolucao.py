# Generated by Django 2.0 on 2018-01-03 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0033_auto_20180102_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evolucao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anotacoes', models.TextField()),
                ('ultimaatualizacao', models.DateTimeField()),
                ('anotacaoconsulta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caps.Consulta')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caps.paciente')),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caps.Profissional')),
            ],
        ),
    ]
