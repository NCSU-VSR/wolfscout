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

    writer = writeHeaders(writer, form_collars_filter, form_weather_filter)

    # if specimen is selected, filter by specimen
    # STILL NEED TO ADD DATE AND TIME FILTER TO BOTH
    if(isSpecimenSelected(form_specimen_name)):
        writer = filterBySpecimen(writer, form_specimen_name, form_collars_filter, form_weather_filter)
    else:
        writer = filterByEverythingElse(writer, form_species_name, form_sex, form_collars_filter, form_weather_filter, isSpeciesSelected(form_species_name), isSexSelected(form_sex))

    return response

def filterBySpecimen(writer, form_specimen_name, form_collars_filter, form_weather_filter):
    specimens = Specimen.objects.all()

    for data in specimens:
        if form_specimen_name.cleaned_data[str(data.common_name)]:
            collarID = data.collar
            dataList = []
            dataValues = data.get_fields()
            for val in dataValues:
                dataList.append(val[1])
            writer = writeCollarWeatherData(writer, str(collarID), dataList, form_collars_filter, form_weather_filter)

    return writer

"""
I'LL CLEAN UP THIS CODE LATER
"""
def filterByEverythingElse(writer, form_species_name, form_sex, form_collars_filter, form_weather_filter, isSpeciesSelected, isSexSelected):
    specimens = Specimen.objects.all()
    species = Species.objects.all()
    for data in species:
        # if species select and no sex
        if isSpeciesSelected and not isSexSelected:
            if form_species_name.cleaned_data[str(data.name)]:
                for specimen in specimens:
                    if str(specimen.species) == str(data.name):
                        collarID = specimen.collar
                        dataList = []
                        dataValues = specimen.get_fields()
                        for val in dataValues:
                            dataList.append(val[1])
                        writer = writeCollarWeatherData(writer, str(collarID), dataList, form_collars_filter, form_weather_filter)
        # if species and sex selected
        if isSpeciesSelected and isSexSelected:
            if form_species_name.cleaned_data[str(data.name)]:
                for specimen in specimens:
                    if str(specimen.species) == str(data.name):
                        writer = filterBySex(writer, specimen, form_sex, form_collars_filter, form_weather_filter)
        # if sex and no species
        if isSexSelected and not isSpeciesSelected:
            for specimen in specimens:
                writer = filterBySex(writer, specimen, form_sex, form_collars_filter, form_weather_filter)
    return writer

def filterBySex(writer, specimen, form_sex, form_collars_filter, form_weather_filter):
    """
    Filters what specimen/species information is exported based on sex
    """
    collarID = specimen.collar
    dataList = []
    dataValues = specimen.get_fields()
    if form_sex.cleaned_data['Male'] and (specimen.sex == 'Male' or specimen.sex == 'male' or specimen.sex == 'M' or specimen.sex == 'm'):
        for val in dataValues:
            dataList.append(val[1])
        writer = writeCollarWeatherData(writer, str(collarID), dataList, form_collars_filter, form_weather_filter)
    if form_sex.cleaned_data['Female'] and (specimen.sex == 'Female' or specimen.sex == 'female' or specimen.sex == 'F' or specimen.sex == 'f'):
        for val in dataValues:
            dataList.append(val[1])
        writer = writeCollarWeatherData(writer, str(collarID), dataList, form_collars_filter, form_weather_filter)
    return writer

def writeCollarWeatherData(writer, collarID, specimenDataList, form_collars_filter, form_weather_filter):
    """
    Retrieves and writer Collar/Weather data if their checkboxes are selected in the DOM
    """
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

def writeHeaders(writer, form_collars_filter, form_weather_filter):
    """
    Writes the headers for the csv field starting wth Specimen, Collars
    and Weather data
    """
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

def isSpecimenSelected(form_specimen_name):
    """
    See's if a specimen is selected in the DOM
    """
    specimens = Specimen.objects.all()
    for specimen in specimens:
        if form_specimen_name.cleaned_data[str(specimen.common_name)]:
            return True
    return False

def isSpeciesSelected(form_species_name):
    """
    Checks to see if a species is selected in the DOM
    """
    species = Species.objects.all()
    for data in species:
        if form_species_name.cleaned_data[str(data.name)]:
            return True
    return False

def isSexSelected(form_sex):
    """
    Checks to see if sex is selected in the DOM
    """
    if form_sex.cleaned_data['Male'] or form_sex.cleaned_data['Female']:
        return True
    return False

def export(request):
    siteDictionary = getDictionary(request)
    if request.method == 'POST':
        form_collars_filter = ExportCollarDataFilterForm(request.POST, error_class=DivErrorList)
        form_weather_filter = ExportWeatherDataFilterForm(request.POST, error_class=DivErrorList)
        form_specimen_filter = ExportWeatherDataFilterForm(request.POST, error_class=DivErrorList)
        form_specimen_name = SpecimenByNameForm(request.POST, error_class=DivErrorList, auto_id='id_specimen_%s')
        form_species_name = SpeciesByNameForm(request.POST, error_class=DivErrorList, auto_id='id_species_%s')
        form_sex = SexForm(request.POST, error_class=DivErrorList)
        if form_specimen_name.is_valid()and form_species_name.is_valid() and form_sex.is_valid() and form_collars_filter.is_valid() and form_weather_filter.is_valid() and form_specimen_filter.is_valid():
            return getCSV(form_specimen_name, form_species_name, form_sex, form_collars_filter, form_weather_filter)
    else:
        specimens = Specimen.objects.all()
        species = Species.objects.all()
        form_collars_filter = ExportCollarDataFilterForm(auto_id='id_collar_filter_%s')
        form_weather_filter = ExportWeatherDataFilterForm(auto_id='id_weather_filter_%s')
        form_specimen_filter = ExportSpecimenFilterForm(auto_id='id_specimen_filter_%s')
        form_specimen_name = SpecimenByNameForm(auto_id='id_specimen_%s')
        form_species_name = SpeciesByNameForm(auto_id='id_species_%s')
        form_sex = SexForm(auto_id='id_sex_%s')
        siteDictionary['specimens'] = specimens
        siteDictionary['species'] = species
        siteDictionary['form_collars_filter'] = form_collars_filter
        siteDictionary['form_weather_filter'] = form_weather_filter
        siteDictionary['form_specimen_filter'] = form_specimen_filter
        siteDictionary['form_specimen_name'] = form_specimen_name
        siteDictionary['form_species_name'] = form_species_name
        siteDictionary['form_sex'] = form_sex

    return render_to_response('export_animal.html', siteDictionary, context_instance=RequestContext(request))
