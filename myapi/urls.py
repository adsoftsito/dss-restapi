# myapi/urls.py

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'estados', views.EstadoViewSet)
router.register(r'municipios', views.MunicipioViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'empresas', views.EmpresaViewSet)

# wire up our API using automatic URL routing
# additionally, we include login URLs for the browsable API

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) 
]

