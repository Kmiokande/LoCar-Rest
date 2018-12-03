from rest_framework.serializers import ModelSerializer
from clientes.models import Cliente


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'sobrenome', 'data_nasc', 'nome_mae', 'cpf',
                  'rg', 'cnh', 'email', 'telefone', 'endereco', 'data_cadastro')
