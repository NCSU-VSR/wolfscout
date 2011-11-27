
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
        if len(the_line) != 14:
            continue
        print the_line
        print "Station Type: " + the_line[5]
        if the_line[5] == "ASOS":
            #station, created = Station.objects.get_or_create(station_code=str(the_line[0]))
            try:
                station = Station.objects.get(station_code=str(the_line[0]))
            except Station.DoesNotExist:
                station = Station()
            #station = Station()
            station.station_code = str(the_line[0])
            station.LOCATION = Point(float(the_line[3]),float(the_line[2]))
            station.name = the_line[1]
            try:
                station.elevation = float(the_line[4])
            except:
                pass
            station.network = the_line[5]
            station.city = the_line[6]
            station.county = the_line[7]
            station.state = the_line[8]
            station.huc = the_line[9]
            station.climatedir = the_line[10]
            station.save()
            print "The station is " + str(station) + "it is at: " + str(station.LOCATION)
    return True

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
    station.distanceToPoint = distance_to_station
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
          "start=" + startDate + "&" \
          "end=" + endDate + "&" \
          "obtype=" + obType + "&" \
          "parameter=" + "all" + "&" \
          "hash=" + settings.CRONOS_API_KEY
    #url = "http://nc-climate.ncsu.edu/dynamic_scripts/cronos/getCRONOSdata.php?station=317079&start=2009-01-01&end=2009-01-01%2003:00:00&obtype=H&parameter=temp,dew,slp&hash="
    #url += settings.CRONOS_API_KEY
    return url

def generateDateTimeString(dataPoint):
    dateString = ""
    dateString += str(dataPoint.LMT_DATETIME.date().year) + "-"
    if dataPoint.LMT_DATETIME.date().month < 10:
        dateString += "0" + str(dataPoint.LMT_DATETIME.date().month) + "-"
    else:
        dateString += str(dataPoint.LMT_DATETIME.date().month) + "-"
    if dataPoint.LMT_DATETIME.date().day < 10:
        dateString += "0" + str(dataPoint.LMT_DATETIME.date().day)
    else:
        dateString += str(dataPoint.LMT_DATETIME.date().day)
    return dateString

def processWeatherData(dataPoint, station, WeatherDataResponse):
    weather_lines = WeatherDataResponse.content.split('\n')
    #First we must remove all metadata
    new_weather_lines = []
    for line in weather_lines:
        if "##" not in line:
            #line is probably worthless
            new_weather_lines.append(line)
    #Now we get the categories
    print "the categories are: "
    categories = new_weather_lines[1].split('|')
    print categories
    #now make a weather point
    print "the weather data is: "
    print new_weather_lines[2]
    weatherData = new_weather_lines[2].split('|')
    weatherDict = {}
    for index, value in enumerate(categories):
        print "Dictionary key is: " + str(value)
        print "Dictionary value is:" + weatherData[index]
        weatherDict[value] = weatherData[index]
    weatherPoint = WeatherDataPoint()

    for key, value in weatherDict.items():
        try:
            print "Key is: " + str(key)
            print "Value is: " + str(value)
            setattr(weatherPoint, key, float(value))
        except:
            continue
    weatherPoint.station = station
    weatherPoint.distance_to_station = station.distanceToPoint
    weatherPoint.save()
    return weatherPoint

def getWeatherData(dataPoint):
    """
    getWeatherData will call getClosestStation and then it will query the
    station to determine the weather data at the given time. Once returned the
    results will be validated and added into the database
    """
    station = getClosestStation(dataPoint=dataPoint)
    dateToSearch = generateDateTimeString(dataPoint)
    print dateToSearch
    url =  buildRequest(station=station, startDate=dateToSearch, endDate=dateToSearch, obType="H")
    print url
    return processWeatherData(dataPoint=dataPoint, station=station,WeatherDataResponse=requests.get(url))


