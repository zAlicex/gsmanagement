from rest_framework import serializers
from .models import CostaRica

class CostaRicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostaRica
        fields = '__all__'
