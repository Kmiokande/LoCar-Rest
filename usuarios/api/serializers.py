from rest_framework.serializers import ModelSerializer
from usuarios.models import Usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('cpf', 'nome', 'data_nasc', 'nome_mae', 'rg', 'cnh', 'email', 'telefone', 'endereco')