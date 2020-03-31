from rest_framework import routers
from .models import Colaboradores
from .serializer import ColaboradoresSerializer
from .viewsets import ColaboradoresViewSet

router = routers.SimpleRouter()
router.register('Colaborador', ColaboradoresViewSet)

urlpatterns = router.urls