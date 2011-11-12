
### Django Imports ####
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.sitemaps import ping_google
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm, ValidationError
from django import forms
from django.template import RequestContext
from django.contrib.gis.shortcuts import render_to_kml
from django.contrib.gis.geos import Point
### Global Imports ####
import datetime
import requests
from geopy.distance import distance as geopy_distance
#### Local Imports ####
from apps.crawler.cronos.models import Station, WeatherDataPoint


##### Views #####
def scrapeStations():
    """
    scrapeStations will make a request to the cronos api. This request will get
    the latest items for the active weather stations and will set all inactive
    stations to the correct state. This is used to ensure we only query valid
    weather stations.

    The staions presently reports the data in the format:
    station|name|lat|lon|elev|network|city|county|state|huc|climdiv|startdate|enddate|active
    """
    print "Scraping Stations with key: " + settings.CRONOS_API_KEY
    req = requests.get('http://www.nc-climate.ncsu.edu/dynamic_scripts/cronos/getCRONOSinventory.php')
    if not req.status_code == 200:
        return 1
    lines = req.content.split('\n')
    lines = lines[16:]
    for line in lines:
        the_line = line.split('|')
        station = Station()
        station.station_code = str(the_line[0])
        station.LOCATION = Point(float(the_line[2]), float(the_line[3]))
        station.name = the_line[1]
        station.elevation = float(the_line[4])
        station.network = the_line[5]
        station.city = the_line[6]
        station.county = the_line[7]
        station.state = the_line[8]
        station.huc = the_line[9]
        station.climatedir = the_line[10]
        station.save()
        print "The station is " + str(station) + "it is at: " + str(station.LOCATION)
    return 0

def getClosestStation(dataPoint):
    """
    getClosestStation will call the above scrape stations method to update the
    database first. After this has been completed it will get the location of
    its data point and compare that against all weather stations. Once the
    closest data point has been found it will return the station and the data
    point.
    """
    all_stations = Station.objects.all()
    distance_to_station = geopy_distance(dataPoint.LOCATION, all_stations[0].LOCATION).kilometers
    the_closest_station = all_stations[0]
    for station in all_stations:
        distance = geopy_distance(dataPoint.LOCATION, station.LOCATION).kilometers
        if distance < distance_to_station:
            distance_to_station = distance
            the_closest_station = station
    print "The closest station was: " + str(the_closest_station)
    print "It was: " + str(distance_to_station) + " kilometers away from the collar data point."
    return station

def buildRequest(station, startDate, endDate, obType):
    """
    buildRequest takes in a few parameters to record the following
    datapoints:
        1. temperature:
        2. humidity
        3. barometric_pressure
        4. precipitation
        5. wind_speed
        6. wind direction
        7. cloud_cover
        8. visibility
        9. sunrise
        10. sunset
        11. heat_index

    All initial parameters are piped into the request and used to
    get back a response that contains all the above information.
    Once built the request url is returned.
    Sample Request:
    http://www.nc-climate.ncsu.edu/dynamic_scripts/cronos/getCRONOSdata.php?station=LAKE&start=2009-08-14&end=2009-08-24&obtype=H&parameter=temp,rh,sr,ws,precip&hash=
    """
    url = "http://www.nc-climate.ncsu.edu/dynamic_scripts/cronos/getCRONOSdata.php?" \
          "station=" + str(station.station_code) + "&" +\
          "start=" + "2009-08-14" + "&" \
          "end=" + "2009-08-24" + "&" \
          "obtype=" + "H" + "&" \
          "parameter=" + "temp,rh,sr,ws,precip" + "&" \
          "hash=" + settings.CRONOS_API_KEY
    url = "http://nc-climate.ncsu.edu/dynamic_scripts/cronos/getCRONOSdata.php?station=317079&start=2009-01-01&end=2009-01-01%2003:00:00&obtype=H&parameter=temp,dew,slp&hash="
    url += settings.CRONOS_API_KEY
    return url

def getWeatherData(dataPoint):
    """
    getWeatherData will call getClosestStation and then it will query the
    station to determine the weather data at the given time. Once returned the
    results will be validated and added into the database
    """
    station = getClosestStation(dataPoint=dataPoint)
    url =  buildRequest(station=station, startDate="fred", endDate="sue", obType="steve")
    return requests.get(url)
