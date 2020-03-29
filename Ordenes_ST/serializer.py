from rest_framework import serializers
from .models import OrdenesSt

class OrdenesStSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenesSt
        fields = '__all__'