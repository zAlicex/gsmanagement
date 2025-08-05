from rest_framework import serializers
from .models import Carga  # Exemplo de modelo

class CargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carga
        fields = '__all__'