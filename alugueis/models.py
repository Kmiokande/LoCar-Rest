from django.db import models
from carros.models import Carro
from clientes.models import Cliente


class Aluguel(models.Model):
    carro = models.OneToOneField(Carro, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    data_aluguel = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return str(self.cliente) + ' - ' + str(self.carro)
