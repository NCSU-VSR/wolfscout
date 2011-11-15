
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
### Local Imports ###
from apps.crawler.gpscollar.collar import CollarParser
from apps.crawler.gpscollar.models import Collar
from apps.crawler.gpscollar.models import CollarData
from apps.general.views import getDictionary
from apps.crawler.gpscollar.forms import collarDataFileForm
from apps.crawler.gpscollar.support import *
from apps.crawler.cronos.models import *
### Views ####

import csv
from django.http import HttpResponse

def getCollarCSV(request, theCollarID):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + theCollarID + '.csv'
    
    theCollar = get_object_or_404(Collar, collarID=theCollarID)
    collarDatas = CollarData.objects.filter(collar=theCollar)
    writer = csv.writer(response)
    
    #writer.writerow(['Collar ID', 'LMT Date/Time', 'Latitude', 'Longitude', 'Height'])
    headerList = []
    #fields = 
    for field in CollarData._meta.fields:
        headerList.append(field.name)
    #Now add the weather fields
    for field in WeatherDataPoint._meta.fields:
        headerList.append(field.name)
    writer.writerow(headerList)
    for data in collarDatas:
        #data.weatherDataPoint.
        writer.writerow([data.collar, data.LMT_DATETIME, data.LATITUDE, data.LONGITUDE, data.HEIGHT])

    return response

def getCollars(request):
    """
    createCollarID first looks up the collar in the db
    to determine if the collar already exists.
    If the collar is not found, it is created.
    After identification or creation, the collar object is added to self.
    """
    collars = Collar.objects.all()
    siteDictionary = getDictionary(request)
    siteDictionary['collars']=collars
    return render_to_response('collar.html', siteDictionary, context_instance=RequestContext(request))
    
def getCollarData(request, theCollarID):
    """
    """
    theCollar = get_object_or_404(Collar, collarID=theCollarID)
    collarDatas = CollarData.objects.filter(collar=theCollar)
    siteDictionary = getDictionary(request)
    siteDictionary['collar'] = theCollar
    siteDictionary['collarDatas']=collarDatas
    return render_to_response('collarData.html', siteDictionary, context_instance=RequestContext(request))
    
from django.forms.util import ErrorList
class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return u''
        return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="messages red"><span></span>%s</div>' % e for e in self])

class CollarIDForm(forms.Form):
    collar_id = forms.ModelChoiceField(Collar.objects.all())

def collarForm(request):
    if request.method == 'POST':
        form = CollarIDForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        if form.is_valid():
            theID = form.cleaned_data['collar_id']
            return HttpResponseRedirect('/collarData/' + str(theID) + "/")
    else:
        form = CollarIDForm()
    return render_to_response('collar.html', {'form': form,}, context_instance=RequestContext(request))

def uploadCollarDataFile(request):
    if request.method == 'POST':
        form = collarDataFileForm(request.POST, request.FILES)
        if form.is_valid():
            processCollarDataFile(request.FILES['file'])
            return HttpResponseRedirect('/')
    else:
        form = collarDataFileForm()
    return render_to_response('uploadCollarData.html', {'form': form},context_instance=RequestContext(request))

def processCollarDataFile(fileToWrite):
    """
    Start by saving the file to disk based on a timestamp
    Then After write has been completed please process the file
    """
    finalFilename = '/opt/webapps/ncsu/collarFiles/'+fileToWrite.name

    destination = open(finalFilename, 'wb+')
    for chunk in fileToWrite.chunks():
        destination.write(chunk)
    destination.close()

    #time to process the file
    cp = CollarParser(finalFilename)
    cp.processCSVIntoDatabase()

    return 0

def getKMLForAllCollarPoints(request, theCollarID):
    theCollar = get_object_or_404(Collar, collarID=theCollarID)
    dataPoints = CollarData.objects.filter(collar=theCollar)
    siteDictionary = getDictionary(request)
    siteDictionary['dataPoints'] = dataPoints
    siteDictionary['theCollar'] = theCollar
    return render_to_kml('dataPoints.kml', siteDictionary, context_instance=RequestContext(request))


def getKMLForAllCollarPointsInteractions(request):
    siteDictionary = {}
    siteDictionary['matches'] = processAllCollars()
    return render_to_kml('interactions.kml', siteDictionary, context_instance=RequestContext(request))

from django.core.urlresolvers import reverse

from djangorestframework.views import View
from djangorestframework.response import Response
from djangorestframework import status

from forms import collarDataFilterForm


class ExampleView(View):
    """
    A basic read-only view that points to 3 other views.
    """

    def get(self, request):
        """
        Handle GET requests, returning a list of URLs pointing to 3 other views.
        """
        return {"Some other resources": [reverse('another-example', kwargs={'num':num}) for num in range(3)]}


class AnotherExampleView(View):
    """
    A basic view, that can be handle GET and POST requests.
    Applies some simple form validation on POST requests.
    """
    form = collarDataFilterForm

    def get(self, request, num):
        """
        Handle GET requests.
        Returns a simple string indicating which view the GET request was for.
        """
        if int(num) > 2:
            return Response(status.HTTP_404_NOT_FOUND)
        return "GET request to AnotherExampleResource %s" % num

    def post(self, request, num):
        """
        Handle POST requests, with form validation.
        Returns a simple string indicating what content was supplied.
        """
        if int(num) > 2:
            return Response(status.HTTP_404_NOT_FOUND)
        return "POST request to AnotherExampleResource %s, with content: %s" % (num, repr(self.CONTENT))