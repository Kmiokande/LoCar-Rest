"""LoCar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from carros.api.viewsets import CarroViewSet
from enderecos.api.viewsets import EnderecoViewSet
from clientes.api.viewsets import ClienteViewSet
from alugueis.api.viewsets import AluguelViewSet

router = routers.DefaultRouter()
# router.register(r'carros', CarroViewSet, base_name='Carro')
router.register(r'carros', CarroViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'alugueis', AluguelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
