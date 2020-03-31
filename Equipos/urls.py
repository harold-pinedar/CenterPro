from rest_framework import routers
# from django.urls import path, include
from .models import TipoEquipo, Marcas, Modelos
from.viewsets import TipoEquipoViewSet, MarcasViewSet, ModelosViewSet



router = routers.SimpleRouter()
router.register('TipoEquipo', TipoEquipoViewSet) 
router.register('Marca', MarcasViewSet)
router.register('Modelo', ModelosViewSet)

urlpatterns = router.urls


