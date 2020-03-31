from rest_framework import routers
from .models import OrdenesSt
from .viewsets import OrdenesStViewSet

router = routers.SimpleRouter()
router.register('OrdenesST', OrdenesStViewSet)

urlpatterns = router.urls