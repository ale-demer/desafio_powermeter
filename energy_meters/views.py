from rest_framework import viewsets, status
from rest_framework import permissions
from django.db.models import Min, Max, Avg, Sum
from rest_framework.decorators import action

from rest_framework.response import Response

from .models import Meter, Measurement
from .serializers import MeterSerializer, MeasurementSerializer


class MeterViewSet(viewsets.ModelViewSet):
    """
    Endpoint para mostrar y crear medidores
    """
    queryset = Meter.objects.all().order_by('-date_added')
    serializer_class = MeterSerializer
    permission_classes = [permissions.AllowAny]
    
    @action(detail=True, methods=['get'])
    def get_max_measure(self, request, pk):
        queryset = Measurement.objects.filter(meter_id=pk).aggregate(max_measure=Max('measure'))
        return Response(queryset)

    @action(detail=True, methods=['get'])
    def get_min_measure(self, request, pk):
        queryset = Measurement.objects.filter(meter_id=pk).aggregate(min_measure=Min('measure'))
        return Response(queryset)

    @action(detail=True, methods=['get'])
    def get_avg_measure(self, request, pk=None):
        queryset = Measurement.objects.filter(meter_id=pk).aggregate(avg_measure=Avg('measure'))
        return Response(queryset)
    
    @action(detail=True, methods=['get'])
    def get_sum_measure(self, request, pk=None):
        queryset = Measurement.objects.filter(meter_id=pk).aggregate(sum_measure=Sum('measure'))
        return Response(queryset)


class MeasurementViewSet(viewsets.ModelViewSet):
    """
    Endpoint para mostrar y crear las mediciones de consumo
    """
    queryset = Measurement.objects.all().order_by('-registry_date')
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.AllowAny]

