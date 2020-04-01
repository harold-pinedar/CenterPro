from rest_framework import viewsets
from .models import OrdenesSt, AnularSt, OrdenEntregadaSt, OrdenReparadaSt
from .serializer import OrdenesStSerializer, AnularStSerializer, OrdenEntregadaStSerializer, OrdenReparadaStSerializer

class OrdenesStViewSet(viewsets.ModelViewSet):
    queryset = OrdenesSt.objects.all()
    serializer_class = OrdenesStSerializer

class AnularStViewSet(viewsets.ModelViewSet):
    queryset = AnularSt.objects.all()
    serializer_class = AnularStSerializer

class OrdenEntregadaStViewSet(viewsets.ModelViewSet):
    queryset = OrdenEntregadaSt.objects.all()
    serializer_class = OrdenEntregadaStSerializer

class OrdenReparadaStViewSet(viewsets.ModelViewSet):
    queryset = OrdenReparadaSt.objects.all()
    serializer_class = OrdenReparadaStSerializer