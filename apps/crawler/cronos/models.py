__author__ = 'chris'

##### Imports #####
from django.contrib.gis.db import models
import datetime

##### Models #####

class WeatherDataPoint(models.Model):
    temperature = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    humidity = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    barometric_pressure =  models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    precipitation = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    wind_speed = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    wind_direction = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    distance_from_collar = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    cloud_cover = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    visibility = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    heat_index = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    extreme_events = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return str(self.id)

class Station(models.Model):
    station_code = models.CharField(max_length=10,null=False, blank=False, unique=True)
    LOCATION = models.PointField()
    name = models.CharField(max_length=100,)
    network = models.CharField(max_length=100,)
    city = models.CharField(max_length=100,)
    country = models.CharField(max_length=100,)
    state = models.CharField(max_length=100,)
    huc = models.CharField(max_length=100,)
    climatedir = models.CharField(max_length=100,)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
