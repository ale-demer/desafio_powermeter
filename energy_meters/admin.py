from django.contrib import admin

from .models import Meter

class MeterAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_added')


# Regitro de modelos para editar desde el Admin
admin.site.register(Meter, MeterAdmin)
