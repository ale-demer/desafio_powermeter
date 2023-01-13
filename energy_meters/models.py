import uuid
from django.db import models
from django.utils.text import slugify


class Meter(models.Model):
    # Clase para la creación de los medidores
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=150, verbose_name="Nombre del medidor")
    date_added = models.DateTimeField( auto_now_add=True )

    class Meta:
        verbose_name = "Medidor"
        ordering = ['id']

    def __str__(self):
        return f'{self.name} ({self.id})'