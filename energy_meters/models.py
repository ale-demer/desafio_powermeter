from django.db import models


class Meter(models.Model):
    # Clase para la creación de los medidores
    id = models.CharField(max_length=16, primary_key=True, verbose_name="ID del medidor")
    name = models.CharField(max_length=150, verbose_name="Nombre del medidor")
    date_added = models.DateTimeField( auto_now_add=True )

    class Meta:
        verbose_name = "medidor"
        verbose_name_plural = 'medidores'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} ({self.id})'


class Measurement(models.Model):
    # Clase para cargar mediciones de consumo de los medidores
    meter = models.ForeignKey(Meter, related_name='measures', on_delete=models.CASCADE)
    registry_date = models.DateTimeField()
    measure = models.PositiveIntegerField()

    class Meta:
        unique_together = ['meter', 'registry_date']
        verbose_name = "medición"
        verbose_name_plural = 'mediciones'
        ordering = ['-registry_date']
    
    def __str__(self):
        return '%s' % (self.measure)
