from rest_framework.serializers import ModelSerializer

from clientes.models import Cliente
from enderecos.api.serializers import EndrecoSerializer
from enderecos.models import Endereco


class ClienteSerializer(ModelSerializer):
    endereco = EndrecoSerializer()

    class Meta:
        model = Cliente
        fields = (
            'id', 'nome', 'sobrenome', 'data_nasc', 'nome_mae', 'cpf', 'rg', 'cnh', 'email', 'telefone',
            'endereco', 'data_cadastro')

    def create(self, validated_data):
        endereco = Endereco.objects.create(**validated_data['endereco'])
        cliente = Cliente.objects.create(endereco=endereco, **validated_data)
        endereco.save()
        cliente.save()
        return cliente

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.sobrenome = validated_data.get('sobrenome', instance.sobrenome)
        instance.data_nasc = validated_data.get('data_nasc', instance.data_nasc)
        instance.nome_mae = validated_data.get('nome_mae', instance.nome_mae)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.rg = validated_data.get('rg', instance.rg)
        instance.email = validated_data.get('email', instance.email)
        instance.telefone = validated_data.get('telefone', instance.telefone)

        instance.save()

        return instance
