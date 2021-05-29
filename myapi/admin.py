from django.contrib import admin
from .models import Hero
from .models import Estado
from .models import Municipio
from .models import Categoria
from .models import Empresa

# Register your models here.

admin.site.register(Hero)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Categoria)
admin.site.register(Empresa)

