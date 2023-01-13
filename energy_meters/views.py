from rest_framework import viewsets
from rest_framework import permissions

from .models import Meter
from .serializers import MeterSerializer


class MeterViewSet(viewsets.ModelViewSet):
    """
    Endpoint para mostrar y editar los medidores
    """
    queryset = Meter.objects.all().order_by('-date_added')
    serializer_class = MeterSerializer
    permission_classes = [permissions.AllowAny]
