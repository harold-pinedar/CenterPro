from django.contrib import admin
from Equipos.models import Marcas, Modelos, TipoEquipo

# Register your models here.

admin.site.register(TipoEquipo)
admin.site.register(Marcas)
admin.site.register(Modelos)