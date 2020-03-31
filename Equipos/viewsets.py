from rest_framework import viewsets
from .models import TipoEquipo, Marcas, Modelos
from .serializer import TipoEquipoSerializer, MarcasSerializer, ModeloSerializer

class TipoEquipoViewSet(viewsets.ModelViewSet):
    queryset = TipoEquipo.objects.all()
    serializer_class = TipoEquipoSerializer

class MarcasViewSet(viewsets.ModelViewSet):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializer

class ModelosViewSet(viewsets.ModelViewSet):
    queryset = Modelos.objects.all()
    serializer_class = ModeloSerializer

