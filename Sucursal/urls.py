from rest_framework import routers
from .models import Sucursal
from .viewsets import SucursalViewSet


router = routers.SimpleRouter()
router.register('Sucursal', SucursalViewSet)

urlpatterns = router.urls