# Generated by Django 2.1.3 on 2018-11-08 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('data_nasc', models.DateField()),
                ('nome_mae', models.CharField(max_length=100)),
                ('rg', models.CharField(max_length=9)),
                ('cnh', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=60)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enderecos.Endereco')),
            ],
        ),
    ]
