from django.shortcuts import render

from rest_framework import viewsets
from .serializers import HeroSerializer
from .serializers import EstadoSerializer
from .serializers import MunicipioSerializer
from .serializers import CategoriaSerializer
from .serializers import EmpresaSerializer

from .models import Hero
from .models import Estado
from .models import Municipio
from .models import Categoria
from .models import Empresa


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all().order_by('idestado')
    serializer_class = EstadoSerializer

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all().order_by('idmunicipio')
    serializer_class = MunicipioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('tipo')
    serializer_class = CategoriaSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all().order_by('idempresa')
    serializer_class = EmpresaSerializer


