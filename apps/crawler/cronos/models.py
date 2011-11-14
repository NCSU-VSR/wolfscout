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
    elevation = models.DecimalField(max_digits=12, decimal_places=2)
    network = models.CharField(max_length=100,)
    city = models.CharField(max_length=100,)
    county = models.CharField(max_length=100,)
    state = models.CharField(max_length=100,)
    huc = models.CharField(max_length=100,)
    climatediv = models.CharField(max_length=100,)
    #start_date = models.DateField()
    #end_date = models.DateField(null=True, blank=True)
    #active = models.BooleanField(default=True)

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
    ##   ob:	observation date/time (EST)
    ##   temp:	Air Temperature (C)
    ##   temp10:	10m Air Temperature (C)
    ##   rh:	Relative Humidity (%)
    ##   rh10:	10m Relative Humidity (%)
    ##   ws:	Wind Speed (m/s)
    ##   ws02:	2m Wind Speed (m/s)
    ##   wd:	Wind Direction (deg)
    ##   wd02:	2m Wind Direction (deg)
    ##   gust:	Wind Gust (m/s)
    ##   precip:	Precipitation (inch)
    ##   pres:	Station Pressure (mb)
    ##   sr:	Solar Radiation (W / m^2)
    ##   par:	Photosynthetically Active Radiation (W / m^2)
    ##   st:	Soil Temperature (C)
    ##   sm:	Soil Moisture (m^3 / m^3)
    ##   leafwetness1:	Experimental Leaf Wetness (??)

    temperature = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    temperature10 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    humidity = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    humidity10 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    barometric_pressure =  models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    precipitation = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    wind_speed = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    wind_speed2 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    wind_direction = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    wind_direction = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    wind_gust = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    solar_radiation = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    photosynthetically_active_radiation = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    soil_temperature = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    soil_moisture = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    leaf_wetness = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    distance_from_collar = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    cloud_cover = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    visibility = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    #sunrise = models.DateTimeField()
    #sunset = models.DateTimeField()
    #heat_index = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    #extreme_events = models.TextField(null=True, blank=True)
    station = models.ForeignKey(Station, null=True, blank=True)

    def __unicode__(self):
        return str(self.id)


