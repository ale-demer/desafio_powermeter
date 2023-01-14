from django.contrib import admin

from .models import Meter, Measurement

class MeterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_added')

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('meter', 'measure', 'registry_date')


# Regitro de modelos para editar desde el Admin
admin.site.register(Meter, MeterAdmin)
admin.site.register(Measurement, MeasurementAdmin)
