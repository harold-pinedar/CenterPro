from rest_framework import viewsets
from .models import Empresas
from .serializer import EmpresasSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer