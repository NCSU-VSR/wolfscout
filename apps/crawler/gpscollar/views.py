
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
from django.http import HttpResponse
### Global Imports ####
import datetime
import csv
### Local Imports ###
from apps.crawler.gpscollar.collar import *
from apps.general.views import getDictionary
from apps.crawler.gpscollar.forms import *
from apps.crawler.gpscollar.support import *
from apps.crawler.cronos.models import *
### Views ####
    
### SCOTT BEGIN ###

def getSingleCollarCSV(request, theCollarID, add_weather, form_collars_filter, form_weather_filter):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + str(theCollarID) + '.csv'

    writer = csv.writer(response)

    writer = createCollarCSV(writer, theCollarID, add_weather, form_collars_filter, form_weather_filter)

    return response

def getMultiCollarCSV(request, form_collars, add_weather, form_collars_filter, form_weather_filter):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=MultiExport.csv'

    writer = csv.writer(response)

    hasValues = False
    collars = Collar.objects.all()
    for collar in collars:
        if form_collars.cleaned_data[str(collar.collarID)]:
            hasValues = True
            writer = createCollarCSV(writer, str(collar.collarID), add_weather, form_collars_filter, form_weather_filter)
    # If at east one checkbox is checked, return csv
    if hasValues:
        return response
    else:
        return HttpResponseRedirect('/collar_export/')

def createCollarCSV(writer, theCollarID, add_weather, form_collars_filter, form_weather_filter):

    theCollar = get_object_or_404(Collar, collarID=theCollarID)
    collarDatas = CollarData.objects.filter(collar=theCollar)

    headerList = []
    for field in CollarData._meta.fields:
        if form_collars_filter.cleaned_data[str(field.name)]:
            headerList.append(field.name)
    #Now add the weather fields
    if add_weather:
        for field in WeatherDataPoint._meta.fields:
            if form_weather_filter.cleaned_data[str(field.name)]:
                headerList.append(field.name)
    writer.writerow(headerList)

    for data in collarDatas:
        dataList = []
        dataValues = data.get_fields()
        for val in dataValues:
            if form_collars_filter.cleaned_data[str(val[0])]:
                dataList.append(val[1])
        if data.weatherDataPoint and add_weather:
            weatherValues = data.weatherDataPoint.get_fields()
            for weatherVal in weatherValues:
                if form_weather_filter.cleaned_data[str(weatherVal[0])]:
                    dataList.append(weatherVal[1])
        writer.writerow(dataList)

    return writer

def export(request):
    siteDictionary = getDictionary(request)
    if request.method == 'POST':
        form_collars = ExportCollarDataForm(request.POST, error_class=DivErrorList, auto_id='%id_s')
        form_collars_filter = ExportCollarDataFilterForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        form_weather_filter = ExportWeatherDataFilterForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        form_export_type = ExportTypeForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        if form_collars.is_valid() and form_collars_filter.is_valid() and form_weather_filter.is_valid() and form_export_type.is_valid():
            is_multi = form_export_type.cleaned_data['is_multi']
            add_weather = form_export_type.cleaned_data['add_weather']
            single_collar = form_export_type.cleaned_data['single_collar']
            if is_multi:
                return getMultiCollarCSV(request, form_collars, add_weather, form_collars_filter, form_weather_filter)
            else:
                return getSingleCollarCSV(request, single_collar, add_weather, form_collars_filter, form_weather_filter)
    else:
        form_collars = ExportCollarDataForm()
        form_collars_filter = ExportCollarDataFilterForm()
        form_weather_filter = ExportWeatherDataFilterForm()
        form_export_type = ExportTypeForm()
        siteDictionary['form_collars'] = form_collars
        siteDictionary['form_collars_filter'] = form_collars_filter
        siteDictionary['form_weather_filter'] = form_weather_filter
        siteDictionary['form_export_type'] = form_export_type
    return render_to_response('collar_export.html', siteDictionary, context_instance=RequestContext(request))
    
def interactions(request):
    siteDictionary = getDictionary(request)
    siteDictionary['collars'] = getCollars(request)
    if request.method == 'POST':
        form = InteractionsDistanceForm(request.POST, request.FILES, error_class=DivErrorList, auto_id='id_%s')
        form_shapeFile = UploadShapeFileForm(request.POST, request.FILES, error_class=DivErrorList, auto_id='id_%s')
        if form.is_valid():
            distance = form.cleaned_data['distance_in_km']
            selectedCollars = form.cleaned_data['selected_collars']
            #print selectedCollars + " " + distance
            #print findAllMatchingByDistance(get_object_or_404(Collar, collarID=selectedCollars), distance)
            #request.FILES['shapes_file']
            #return HttpResponseRedirect('/collarData/' + str(theID) + "/")
    else:
        form = InteractionsDistanceForm()
        form_shapeFile = UploadShapeFileForm()
        form.fields['distance_in_km'].widget.attrs['disabled'] = True
    siteDictionary['form'] = form
    siteDictionary['form_shapeFile'] = form_shapeFile
    return render_to_response('collar_interactions.html', siteDictionary, context_instance=RequestContext(request))

def getCollars(request):
    collars = Collar.objects.all()
    return collars
    
def getCollarData(request, theCollarID):
    siteDictionary = getDictionary(request)
    siteDictionary['collar'] = get_object_or_404(Collar, collarID=theCollarID)
    siteDictionary['collarDatas']=CollarData.objects.filter(collar=theCollar)
    return render_to_response('collar_data.html', siteDictionary, context_instance=RequestContext(request))

def collarForm(request):
    if request.method == 'POST':
        form = CollarIDForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        if form.is_valid():
            theID = form.cleaned_data['collar_id']
            return HttpResponseRedirect('/collarData/' + str(theID) + "/")
    else:
        form = CollarIDForm()
    return render_to_response('collar.html', {'form': form,}, context_instance=RequestContext(request))
    
### SCOTT END ###

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