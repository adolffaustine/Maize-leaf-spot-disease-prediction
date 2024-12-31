from rest_framework import serializers
from .models import Maize

class MaizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maize
        fields = '__all__' 