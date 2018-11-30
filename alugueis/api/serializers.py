from rest_framework.serializers import ModelSerializer
from alugueis.models import Aluguel


class AluguelSerializer(ModelSerializer):
    class Meta:
        model = Aluguel
        fields = ('carro', 'cliente', 'data_aluguel', 'data_devolucao', 'preco')
