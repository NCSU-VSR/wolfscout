### Django Imports ####
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.sitemaps import ping_google
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
### Global Imports ####
import datetime
### Local Imports ####
from apps.study.models import Study
### Views ####

@login_required()
def index(request):
    """
    """
    siteDictionary = getDictionary(request)
    return render_to_response('index.html', siteDictionary, context_instance=RequestContext(request))
    
def getDictionary(request):
    siteDictionary = {}
    siteDictionary['request'] = request
    siteDictionary['STATIC_URL'] = settings.STATIC_URL
    ### Required data for all pages ###
    myStudies = Study.objects.all().filter(owner=request.user) ### Creates object
    siteDictionary['myStudies']=myStudies
    siteDictionary['allStudies'] = Study.objects.all()
    return siteDictionary

def getClimateDictionary():
    climateDictionary = {
        # NEED ENTRIES FOR THESE:
        "id" : ("ID", ""),
        "distance_to_station" : ("Distance to Station", "(km)"),
        "station" : ("Station", ""),
        #####
        "lev1" : ("Level 1 Cloud Type / Height", ""),
        "lev2" : ("Level 2 Cloud Type / Height", ""),
        "lev3" : ("Level 3 Cloud Type / Height", ""),
        "ob" : ("observation date/time", "EST"),
        "temp" : ("Air Temperature", "(C)"),
        "tempmin" : ("Past Hour Min Temperature" , "(C)"),
        "tempmax" : ("Past Hour Max Temperature" , "(C)"),
        "tempavg" : ("Past Hour Avg Temperature" , "(C)"),
        "temp10" : ("10m Air Temperature", "(C)"),
        "temp10min" : ("Past Hour Min 10m Air Temperature", "(C)"),
        "temp10max" : ("Past Hour Max 10m Air Temperature", "(C)"),
        "temp10avg" : ("Past Hour Avg 10m Air Temperature", "(C)"),
        "tempmax6" : ("6 Hour Max Temperature", "(C)"),
        "tempmin6" : ("6 Hour Min Temperature", "(C)"),
        "tempmax24" : ("24 Hour Max Temperature", "(C)"),
        "tempmin24" : ("24 Hour Min Temperature", "(C)"),
        "rh" : ("Relative Humidity", "(%)"),
        "dew" : ("Dewpoint Temperature", "(C)"),
        "ws" : ("Wind Speed", "(m/s)"),
        "wd" : ("Wind Direction", "(deg)"),
        "gust" : ("Wind Gusts", "(m/s)"),
        "precip" : ("Hourly Precipitation", "(inch)"),
        "precip6" : ("3/6 Hour Precipitation", "(inch)"),
        "precip24" : ("24 Hour Total Precipitation", "(inch)"),
        "slp" : ("Sea Level Pressure", ""),
        "levl1" : ("Level 1 Cloud Type / Height", ""),
        "levl2" : ("Level 2 Cloud Type / Height", ""),
        "levl3" : ("Level 3 Cloud Type / Height", ""),
        "vis" : ("Visibility", "(sm)"),
        "weather" : ("Present Weather", ""),
        "obscur" : ("Obscuration", ""),
        "altimeter" : ("Altimeter Setting", "(in. hg)"),
        "presch" : ("Pressure Change", "(mb)"),
        "pind" : ("Pressure Indicator", ""),
        "groundsnow" : ("Snow On Ground", "(inch)"),
        "remarks" : ("METAR Remarks", ""),
        "rhmin" : ("Past Hour Min Relative Humidity", "(%)"),
        "rhmax" : ("Past Hour Max Relative Humidity", "(%)"),
        "rhavg" : ("Past Hour Avg Relative Humidity", "(%)"),
        "rh10" : ("10m Relative Humidity", "(C)"),
        "rh10min" : ("Past Hour Min 10m Relative Humidity", "(%)"),
        "rh10max" : ("Past Hour Max 10m Relative Humidity", "(%)"),
        "rh10avg" : ("Past Hour Avg 10m Relative Humidity", "(%)"),
        "wsavg" : ("Past Hour Avg Wind Speed", "(m/s)"),
        "ws02" : ("2m Wind Speed", "(m/s)"),
        "ws02avg" : ("Past Hour Avg 2m Wind Speed", "(m/s)"),
        "wdavg" : ("Past Hour Avg Wind Direction", "(deg)"),
        "wd02" : ("2m Wind Direction", "(deg)"),
        "wd02avg" : ("Past Hour Avg 2m Wind Direction", "(deg)"),
        "gustavg" : ("Past Hour Avg Wind Gusts", "(m/s)"),
        "pres" : ("Station Pressure", "(mb)"),
        "presmin" : ("Past Hour Min Station Pressure", "(mb)"),
        "presmax" : ("Past Hour Max Station Pressure", "(mb)"),
        "presavg" : ("Past Hour Avg Station Pressure", "(mb)"),
        "sr" : ("Solar Radiation", "(W / m^2)"),
        "srmin" : ("Past Hour Min Solar Radiation", "(W / m^2)"),
        "srmax" : ("Past Hour Max Solar Radiation", "(W / m^2)"),
        "sravg" : ("Past Hour Avg Solar Radiation", "(W / m^2)"),
        "par" : ("Photosynthetically Active Radation", "(W / m^2)"),
        "parmin" : ("Past Hour Min Photosynthetically Active Radiation ", "(W / m^2)"),
        "parmax" : ("Past Hour Max Photosynthetically Active Radiation ", "(W / m^2)"),
        "paravg" : ("Past Hour Avg Photosynthetically Active Radiation ", "(W / m^2)"),
        "st" : ("Soil Temperature", "(C)"),
        "stmin" : ("Past Hour Min Soil Temperature ", "(C)"),
        "stmax" : ("Past Hour Max Soil Temperature ", "(C)"),
        "stavg" : ("Past Hour Avg Soil Temperature ", "(C)"),
        "sm" : ("Soil Moisture", "(m^3 / m^3)"),
        "smmin" : ("Past Hour Min Soil Moisture", "(m^3 / m^3)"),
        "smmax" : ("Past Hour Max Soil Moisture", "(m^3 / m^3)"),
        "smavg" : ("Past Hour Avg Soil Moisture", "(m^3 / m^3)"),
        "leafwetness1" : ("Experimental Leaf Wetness", "(??)")
    }
    return climateDictionary