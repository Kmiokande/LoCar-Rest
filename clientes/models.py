from django.db import models
from enderecos.models import Endereco


class Cliente(models.Model):
    nome = models.CharField(max_length=40)
    sobrenome = models.CharField(max_length=150)
    data_nasc = models.DateField()
    nome_mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9, unique=True)
    cnh = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=40, unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome + ' - ' + self.cpf
