# Generated by Django 2.1.3 on 2018-12-06 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alugueis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluguel',
            name='concluido',
            field=models.BooleanField(default=False),
        ),
    ]