from rest_framework.serializers import ModelSerializer
from clientes.models import Cliente


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('cpf', 'nome', 'data_nasc', 'nome_mae', 'rg', 'cnh', 'telefone', 'endereco', 'data_cadastro')
