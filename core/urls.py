from django.contrib import admin
from rest_framework import routers
from django.urls import include,path

from energy_meters import views


router = routers.DefaultRouter()
router.register(r'meters', views.MeterViewSet, basename="meter")
router.register(r'measurements', views.MeasurementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]