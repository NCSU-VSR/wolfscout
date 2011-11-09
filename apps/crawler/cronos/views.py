
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
### Global Imports ####
import datetime
import requests
#### Local Imports ####
from apps.crawler.cronos.models import Station, WeatherDataPoint


##### Views #####
def scrapeStations():
    """
    scrapeStations will make a request to the cronos api. This request will get
    the latest items for the active weather stations and will set all inactive
    stations to the correct state. This is used to ensure we only query valid
    weather stations.
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
        print "The station is " + str(station)
    return 0

def getClosestStation(dataPoint):
    """
    getClosestStation will call the above scrape stations method to update the
    database first. After this has been completed it will get the location of
    its data point and compare that against all weather stations. Once the
    closest data point has been found it will return the station and the data
    point.
    """
    return 0

def getWeatherData(dataPoint):
    """
    getWeatherData will call getClosestStation and then it will query the
    station to determine the weather data at the given time. Once returned the
    results will be validated and added into the database
    """
    return 0
