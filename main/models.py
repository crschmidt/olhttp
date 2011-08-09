from django.contrib.gis.db import models

# Create your models here.

class Data(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    geometry = models.GeometryField(srid=4326)
    objects = models.GeoManager()
