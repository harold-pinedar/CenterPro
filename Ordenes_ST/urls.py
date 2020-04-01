from rest_framework import routers
##from .models import OrdenesSt, AnularSt, OrdenEntregadaSt, OrdenReparadaSt
from .viewsets import OrdenesStViewSet, AnularStViewSet, OrdenEntregadaStViewSet, OrdenReparadaStViewSet

router = routers.SimpleRouter()
router.register('OrdenesST', OrdenesStViewSet)
router.register("AnularST",AnularStViewSet)
router.register("OrdenEntregadaST",OrdenEntregadaStViewSet)
router.register("OrdenReparadaST",OrdenReparadaStViewSet)
urlpatterns = router.urls