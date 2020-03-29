from rest_framework import serializers
from .models import TipoEquipo, Marcas, Modelos

class TipoEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEquipo
        fields = '__all__'


class MarcasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marcas
        fields = '__all__'


class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelos
        fields = '__all__'

