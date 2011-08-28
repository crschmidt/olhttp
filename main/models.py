from django.contrib.gis.db import models

# Create your models here.

class Paddocks(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    number = models.FloatField()
    owner = models.CharField(max_length=50)
    acres = models.FloatField()
    date_added = models.CharField(max_length=25)
    notes = models.CharField(max_length=250)
    links = models.CharField(max_length=100)
    photo_vid_links = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=50)
    pm_success = models.CharField(max_length=100)
    pm_problem = models.CharField(max_length=100)
    pm_plans = models.CharField(max_length=100) 
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
    notes = models.CharField(max_length=250)
    links = models.CharField(max_length=100)
    photo_vid_links = models.CharField(max_length=100)
    wcm_success = models.CharField(max_length=100)
    wcm_problem = models.CharField(max_length=100)
    wcm_plans = models.CharField(max_length=100)
    the_geom = models.MultiPolygonField(srid=-1)
    objects = models.GeoManager()
    class Meta:
        db_table = u'properties'

class Cells(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    number = models.FloatField()
    owner = models.CharField(max_length=50)
    acres = models.FloatField()
    date_added = models.CharField(max_length=25)
    notes = models.CharField(max_length=250)
    links = models.CharField(max_length=100)
    photo_vid_links = models.CharField(max_length=100)
    wcm_success = models.CharField(max_length=100)
    wcm_problem = models.CharField(max_length=100)
    wcm_plans = models.CharField(max_length=100)
    the_geom = models.MultiPolygonField(srid=-1)
    objects = models.GeoManager()
    class Meta:
        db_table = u'cells'

