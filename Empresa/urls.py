from rest_framework import routers
from .models import Empresas
from .viewsets import EmpresasViewSet

router = routers.SimpleRouter()
router.register('Empresa', EmpresasViewSet)

urlpatterns = router.urls