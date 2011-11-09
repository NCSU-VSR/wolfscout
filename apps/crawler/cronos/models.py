__author__ = 'chris'

##### Imports #####
from django.contrib.gis.db import models
import datetime

##### Models #####
class Station(models.Model):
    """
    Station is used to keep tabs on every station known about in the CRONOS api
    developed @NCSU. These items allow us to easily identify which stations are
    active and are reporting the most useful data to us.
    """
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

    def __unicode__(self):
        return str(self.station_code)

class WeatherDataPoint(models.Model):
    """
    WeatherDataPoint is designed to store a data point object from a weather
    station that will map to a particular collar data point. Each CollarData
    point will only have one weather data point mapping. The information
    recorded here is according the specifications developed by Dr. Lauren
    Charles Smith.
    """
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
    station = models.ForeignKey(Station, null=True, blank=True)

    def __unicode__(self):
        return str(self.id)


