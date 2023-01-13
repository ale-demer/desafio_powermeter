from rest_framework import serializers
from .models import Meter

class MeterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meter
        fields = ['id', 'name']