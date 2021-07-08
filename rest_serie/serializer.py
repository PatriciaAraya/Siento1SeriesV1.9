from rest_framework import serializers
from core.models import Series

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['nombre', 'genero', 'imagen', 'plataforma']