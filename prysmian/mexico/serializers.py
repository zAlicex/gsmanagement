from rest_framework import serializers
from .models import Mexico

class MexicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mexico
        fields = '__all__'
