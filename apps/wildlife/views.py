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
from apps.wildlife.forms import *
from apps.crawler.gpscollar.support import *
from apps.crawler.cronos.models import *

def getCSV(form_specimen_name, form_species_name, form_sex, form_collars_filter, form_weather_filter):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=ExportBySpecimen.csv'

    writer = csv.writer(response)

    writer = writeHeaders(writer, form_specimen_name, form_collars_filter, form_weather_filter)

    writer = iterateThroughFilterHierarchy(writer, form_specimen_name, form_collars_filter, form_weather_filter)

    return response

def writeHeaders(writer, form_specimen_name, form_collars_filter, form_weather_filter):

    headerList = []
    for field in Specimen._meta.fields:
        headerList.append(field.name)
    for field in CollarData._meta.fields:
        if form_collars_filter.cleaned_data[str(field.name)]:
            headerList.append(field.name)
    for field in WeatherDataPoint._meta.fields:
        if form_weather_filter.cleaned_data[str(field.name)]:
            headerList.append(field.name)
    writer.writerow(headerList)

    return writer


def iterateThroughFilterHierarchy(writer, form_specimen_name, form_collars_filter, form_weather_filter):
    specimens = Specimen.objects.all()

    for data in specimens:
        if form_specimen_name.cleaned_data[str(data.pk)]:
            collarID = data.collar
            dataList = []
            dataValues = data.get_fields()
            for val in dataValues:
                dataList.append(val[1])
            writer = writeCollarWeatherData(writer, str(collarID), dataList, form_collars_filter, form_weather_filter)

    return writer

def writeCollarWeatherData(writer, collarID, specimenDataList, form_collars_filter, form_weather_filter):
    theCollar = get_object_or_404(Collar, collarID=collarID)
    collarDatas = CollarData.objects.filter(collar=theCollar)
    for data in collarDatas:
        dataList = specimenDataList[:]
        dataValues = data.get_fields()
        for val in dataValues:
            if form_collars_filter.cleaned_data[str(val[0])]:
                dataList.append(val[1])
        if data.weatherDataPoint:
            weatherValues = data.weatherDataPoint.get_fields()
            for weatherVal in weatherValues:
                if form_weather_filter.cleaned_data[str(weatherVal[0])]:
                    dataList.append(weatherVal[1])
        writer.writerow(dataList)

    return writer

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
        form_collars_filter = ExportCollarDataFilterForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        form_weather_filter = ExportWeatherDataFilterForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        form_specimen_name = SpecimenByNameForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        form_species_name = SpeciesByNameForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        form_sex = SexForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        if form_specimen_name.is_valid() and form_collars_filter.is_valid() and form_weather_filter.is_valid():
            return getCSV(form_specimen_name, form_species_name, form_sex, form_collars_filter, form_weather_filter)
    else:
        specimens = Specimen.objects.all()
        species = Species.objects.all()
        form_collars_filter = ExportCollarDataFilterForm()
        form_weather_filter = ExportWeatherDataFilterForm()
        form_specimen_name = SpecimenByNameForm()
        form_species_name = SpeciesByNameForm()
        form_sex = SexForm()
        siteDictionary['specimens'] = specimens
        siteDictionary['species'] = species
        siteDictionary['form_collars_filter'] = form_collars_filter
        siteDictionary['form_weather_filter'] = form_weather_filter
        siteDictionary['form_specimen_name'] = form_specimen_name
        siteDictionary['form_species_name'] = form_species_name
        siteDictionary['form_sex'] = form_sex
    return render_to_response('export_specimen.html', siteDictionary, context_instance=RequestContext(request))

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