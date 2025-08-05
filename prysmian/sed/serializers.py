from rest_framework import serializers
from .models import Sed

class SedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sed
        fields = '__all__'
