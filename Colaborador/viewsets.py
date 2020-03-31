from rest_framework import viewsets
from .serializer import ColaboradoresSerializer
from .models import Colaboradores


class ColaboradoresViewSet(viewsets.ModelViewSet):
    queryset = Colaboradores.objects.all()
    serializer_class = ColaboradoresSerializer