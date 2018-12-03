# Generated by Django 2.1.3 on 2018-12-03 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('sobrenome', models.CharField(max_length=150)),
                ('data_nasc', models.DateField()),
                ('nome_mae', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(max_length=9, unique=True)),
                ('cnh', models.CharField(max_length=11, unique=True)),
                ('email', models.CharField(max_length=40, unique=True)),
                ('telefone', models.CharField(max_length=15)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='enderecos.Endereco')),
            ],
        ),
    ]
