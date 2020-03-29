from rest_framework import viewsets
from .models import OrdenesSt
from .serializer import OrdenesStSerializer

class OrdenesStViewSet(viewsets.ModelViewSet):
    queryset = OrdenesSt.objects.all()
    serializer_class = OrdenesStSerializer