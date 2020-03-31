from rest_framework import routers
from .models import Cliente
from .viewsets import ClienteViewSet
from .serializer import ClienteSerializer

router = routers.SimpleRouter()
router.register("Cliente", ClienteViewSet)

urlpatterns = router.urls