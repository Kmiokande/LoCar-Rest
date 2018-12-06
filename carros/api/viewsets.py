from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from carros.models import Carro
from .serializers import CarroSerializer


class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'disponivel')
