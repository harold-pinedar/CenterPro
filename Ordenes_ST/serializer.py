from rest_framework import serializers
from .models import OrdenesSt, AnularSt, OrdenEntregadaSt, OrdenReparadaSt

class OrdenesStSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenesSt
        fields = '__all__'

class AnularStSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnularSt
        fields = '__all__'

class OrdenEntregadaStSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenEntregadaSt
        fields = '__all__'

class OrdenReparadaStSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenReparadaSt
        fields = '__all__'