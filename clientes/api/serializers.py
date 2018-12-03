from rest_framework.serializers import ModelSerializer
from clientes.models import Cliente


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nome', 'sobrenome', 'data_nasc', 'nome_mae', 'cpf',
                  'rg', 'cnh', 'telefone', 'endereco', 'data_cadastro')
