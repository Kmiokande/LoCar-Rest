from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    bairro = models.CharField(max_length=60)
    complemento = models.CharField(max_length=60, null=True, blank=True)
    cidade = models.CharField(max_length=60)
    cep = models.CharField(max_length=9)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.logradouro + ' - ' + self.complemento + ' - ' + self.cidade
