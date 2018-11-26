from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco


class EndrecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'logradouro', 'numero', 'bairro', 'complemento', 'cidade', 'cep', 'estado')
