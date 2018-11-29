from rest_framework.serializers import ModelSerializer
from clientes.models import Cliente


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('usuario', 'cpf', 'nome', 'data_nasc', 'nome_mae', 'rg', 'cnh', 'email', 'telefone', 'endereco')
