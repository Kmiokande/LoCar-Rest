from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EndrecoSerializer

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EndrecoSerializer