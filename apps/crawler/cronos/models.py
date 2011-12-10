### Standard Library Imports
import datetime
### Django Imports
from django.core.exceptions import ValidationError
from django.contrib.gis.db import models
### Project Imports


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
    elevation = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
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
    
    def get_fields(self):
        # make a list of field/values.
        return [(field.name, field.value_to_string(self)) for field in Station._meta.fields]

class WeatherDataPoint(models.Model):
    """
    WeatherDataPoint is designed to store a data point object from a weather
    station that will map to a particular collar data point. Each CollarData
    point will only have one weather data point mapping. The information
    recorded here is according the specifications developed by Dr. Lauren
    Charles Smith.

    Full List of weather Parameters

    altimeter
    dew
    groundsnow
    gust
    gustavg
    lev1
    lev2
    lev3
    obscur
    par
    paravg
    parmax
    parmin
    pind
    precip
    precip24
    precip6
    pres
    presavg
    presch
    presmax
    presmin
    remarks
    rh
    rh10
    rh10avg
    rh10max
    rh10min
    rhavg
    rhmax
    rhmin
    slp
    sm
    smavg
    smmax
    smmin
    sr
    sravg
    srmax
    srmin
    st
    stavg
    stmax
    stmin
    temp
    temp10
    temp10avg
    temp10max
    temp10min
    tempavg
    tempmax
    tempmax24
    tempmax6
    tempmin
    tempmin24
    tempmin6
    vis
    wd
    wd02
    wd02avg
    wdavg
    weather
    ws
    ws02
    ws02avg
    wsavg
    """

    altimeter = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    dew = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    groundsnow = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    gust = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    gustavg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    lev1 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    lev2 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    lev3 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    obscur = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    par = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    paravg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    parmax = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    parmin = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    pind = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    precip = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    precip24 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    precip6 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    pres = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    presavg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    presch = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    presmax = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    presmin = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    rh = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    rh10 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    rh10avg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    rh10max = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    rh10min = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    rhavg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    rhmax = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    rhmin = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    slp = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    sm = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    smavg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    smmax = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    smmin = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    sr = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    sravg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    srmax = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    srmin = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    st = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    stavg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    stmax = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    stmin = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    temp = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    temp10 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    temp10avg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    temp10max = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    temp10min = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    tempavg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    tempmax = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    tempmax24 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    tempmax6 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    tempmin = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    tempmin24 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    tempmin6 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    vis = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    wd = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    wd02 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    wd02avg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    wdavg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    weather = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    ws = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    ws02 = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    ws02avg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    wsavg = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    #sunrise = models.DateTimeField()
    #sunset = models.DateTimeField()
    #heat_index = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    #extreme_events = models.TextField(null=True, blank=True)
    distance_to_station = models.DecimalField(max_digits=12, decimal_places=7, null=True, blank=True)
    station = models.ForeignKey(Station, null=True, blank=True)

    def __unicode__(self):
        return str(self.id)

    def get_fields(self):
        # make a list of field/values.
        return [(field.name, field.value_to_string(self)) for field in WeatherDataPoint._meta.fields]


