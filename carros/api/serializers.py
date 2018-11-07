from rest_framework.serializers import ModelSerializer
from carros.models import Carro

class CarroSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = ('placa', 'modelo', 'cor', 'ano', 'renavam', 'preco')