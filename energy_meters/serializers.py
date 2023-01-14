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

    def validate_measure(self, value):
        """
        Verifica si el valor de la medida es positivo.
        """
        if value < 0:
            raise serializers.ValidationError("El valor debe ser mayor a cero.")
        return value
