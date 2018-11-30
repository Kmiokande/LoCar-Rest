# Generated by Django 2.1.3 on 2018-11-29 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carros', '0004_auto_20181129_1918'),
        ('clientes', '0008_remove_cliente_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_aluguel', models.DateField(auto_now_add=True)),
                ('data_devolucao', models.DateField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('carro', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='carros.Carro')),
                ('cliente', models.ManyToManyField(to='clientes.Cliente')),
            ],
        ),
    ]