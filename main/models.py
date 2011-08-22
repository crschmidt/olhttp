from django.contrib.gis.db import models

# Create your models here.

class Paddocks(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    number = models.FloatField()
    owner = models.CharField(max_length=50)
    acres = models.FloatField()
    date_added = models.CharField(max_length=25)
    notes = models.CharField(max_length=10)
    links = models.CharField(max_length=10)
    the_geom = models.MultiPolygonField(srid=-1)
    objects = models.GeoManager()
    class Meta:
        db_table = u'paddocks'

class Properties(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    number = models.FloatField()
    owner = models.CharField(max_length=50)
    acres = models.FloatField()
    date_added = models.CharField(max_length=25)
    notes = models.CharField(max_length=10)
    links = models.CharField(max_length=10)
    the_geom = models.MultiPolygonField(srid=-1)
    objects = models.GeoManager()
    class Meta:
        db_table = u'properties'

