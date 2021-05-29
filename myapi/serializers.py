# serializers.py

from rest_framework import serializers
from .models import Hero
from .models import Estado
from .models import Municipio
from .models import Categoria
from .models import Empresa

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name','alias')

class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ('idestado','estado')

class MunicipioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Municipio
        fields = ('idmunicipio','identidad','nombremunicipio')

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('tipo','descripcion')

class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empresa
        fields = ('idempresa','identidad','idmunicipio','codigoactividad','nombreempresa','latitud','longitud',	'calle', 'numero','colonia','codigopostal','ciudad','estado','descripcion')


