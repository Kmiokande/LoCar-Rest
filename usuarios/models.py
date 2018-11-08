from django.db import models
from enderecos.models import Endereco

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    nome_mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, primary_key=True)  # CPF chave primária
    rg = models.CharField(max_length=9)
    cnh = models.CharField(max_length=11)
    email = models.CharField(max_length=60)
    telefone = models.CharField(max_length=15)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome