from rest_framework.viewsets import ModelViewSet
from usuarios.models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
