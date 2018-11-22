from rest_framework.viewsets import ModelViewSet
from carros.models import Carro
from .serializers import CarroSerializer


class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
