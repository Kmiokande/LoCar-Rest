from django.db import models


class Carro(models.Model):
    modelo = models.CharField(max_length=60)
    cor = models.CharField(max_length=15)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    placa = models.CharField(max_length=8, unique=True)
    renavam = models.CharField(max_length=11, unique=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.modelo + ' - ' + self.placa
