from django.db import models
from enderecos.models import Endereco
from django.contrib.auth.models import Group, User


class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    nome_mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, primary_key=True)  # CPF chave primária
    rg = models.CharField(max_length=9, unique=True)
    cnh = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + ' - ' + self.cpf
