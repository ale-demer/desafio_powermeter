from rest_framework import serializers
from .models import Meter, Measurement


class MeterSerializer(serializers.HyperlinkedModelSerializer):
    measures = serializers.StringRelatedField(many=True)

    class Meta:
        model = Meter
        fields = ['id', 'name', 'measures']


class MeasurementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Measurement
        fields = ['meter', 'measure', 'registry_date']
