from rest_framework import viewsets
from .models import Sucursal
from .serializer import SucursalSerializer


class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer