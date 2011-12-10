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

def getCSV(form_animal_name, form_species_name, form_sex, form_collars_filter, form_weather_filter):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=ExportByAnimal.csv'

    writer = csv.writer(response)

    writer = writeHeaders(writer, form_collars_filter, form_weather_filter)

    # if specimen is selected, filter by specimen
    # STILL NEED TO ADD DATE AND TIME FILTER TO BOTH
    if(isAnimalSelected(form_animal_name)):
        writer = filterByAnimal(writer, form_animal_name, form_collars_filter, form_weather_filter)
    else:
        writer = filterByEverythingElse(writer, form_species_name, form_sex, form_collars_filter, form_weather_filter, isSpeciesSelected(form_species_name), isSexSelected(form_sex))

    return response

def filterByAnimal(writer, form_animal_name, form_collars_filter, form_weather_filter):
    animals = Animal.objects.all()

    for data in animals:
        if form_animal_name.cleaned_data[str(data.common_name)]:
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
    animals = Animal.objects.all()
    species = Species.objects.all()
    for data in species:
        # if species select and no sex
        if isSpeciesSelected and not isSexSelected:
            if form_species_name.cleaned_data[str(data.name)]:
                for animal in animals:
                    if str(animal.species) == str(data.name):
                        collarID = animal.collar
                        dataList = []
                        dataValues = animal.get_fields()
                        for val in dataValues:
                            dataList.append(val[1])
                        writer = writeCollarWeatherData(writer, str(collarID), dataList, form_collars_filter, form_weather_filter)
        # if species and sex selected
        if isSpeciesSelected and isSexSelected:
            if form_species_name.cleaned_data[str(data.name)]:
                for animal in animals:
                    if str(animal.species) == str(data.name):
                        writer = filterBySex(writer, animal, form_sex, form_collars_filter, form_weather_filter)
        # if sex and no species
        if isSexSelected and not isSpeciesSelected:
            for animal in animals:
                writer = filterBySex(writer, animal, form_sex, form_collars_filter, form_weather_filter)
    return writer

def filterBySex(writer, animal, form_sex, form_collars_filter, form_weather_filter):
    """
    Filters what specimen/species information is exported based on sex
    """
    collarID = animal.collar
    dataList = []
    dataValues = animal.get_fields()
    if form_sex.cleaned_data['Male'] and (animal.sex == 'Male' or animal.sex == 'male' or animal.sex == 'M' or animal.sex == 'm'):
        for val in dataValues:
            dataList.append(val[1])
        writer = writeCollarWeatherData(writer, str(collarID), dataList, form_collars_filter, form_weather_filter)
    if form_sex.cleaned_data['Female'] and (animal.sex == 'Female' or animal.sex == 'female' or animal.sex == 'F' or animal.sex == 'f'):
        for val in dataValues:
            dataList.append(val[1])
        writer = writeCollarWeatherData(writer, str(collarID), dataList, form_collars_filter, form_weather_filter)
    return writer

def writeCollarWeatherData(writer, collarID, animalDataList, form_collars_filter, form_weather_filter):
    """
    Retrieves and writer Collar/Weather data if their checkboxes are selected in the DOM
    """
    theCollar = get_object_or_404(Collar, collarID=collarID)
    collarDatas = CollarData.objects.filter(collar=theCollar)
    for data in collarDatas:
        dataList = animalDataList[:]
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
    for field in Animal._meta.fields:
        headerList.append(field.name)
    for field in CollarData._meta.fields:
        if form_collars_filter.cleaned_data[str(field.name)]:
            headerList.append(field.name)
    for field in WeatherDataPoint._meta.fields:
        if form_weather_filter.cleaned_data[str(field.name)]:
            headerList.append(field.name)
    writer.writerow(headerList)

    return writer

def isAnimalSelected(form_animal_name):
    """
    See's if a specimen is selected in the DOM
    """
    animals = Animal.objects.all()
    for animal in animals:
        if form_animal_name.cleaned_data[str(animal.common_name)]:
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
        form_animal_filter = ExportAnimalFilterForm(request.POST, error_class=DivErrorList)
        form_animal_name = AnimalByNameForm(request.POST, error_class=DivErrorList, auto_id='id_animal_%s')
        form_species_name = SpeciesByNameForm(request.POST, error_class=DivErrorList, auto_id='id_species_%s')
        form_sex = SexForm(request.POST, error_class=DivErrorList)
        if form_animal_name.is_valid()and form_species_name.is_valid() and form_sex.is_valid() and form_collars_filter.is_valid() and form_weather_filter.is_valid() and form_animal_filter.is_valid():
            return getCSV(form_animal_name, form_species_name, form_sex, form_collars_filter, form_weather_filter)
    else:
        animals = Animal.objects.all()
        species = Species.objects.all()
        form_collars_filter = ExportCollarDataFilterForm(auto_id='id_collar_filter_%s')
        form_weather_filter = ExportWeatherDataFilterForm(auto_id='id_weather_filter_%s')
        form_animal_filter = ExportAnimalFilterForm(auto_id='id_animal_filter_%s')
        form_animal_name = AnimalByNameForm(auto_id='id_animal_%s')
        form_species_name = SpeciesByNameForm(auto_id='id_species_%s')
        form_sex = SexForm(auto_id='id_sex_%s')
        siteDictionary['animals'] = animals
        siteDictionary['species'] = species
        siteDictionary['form_collars_filter'] = form_collars_filter
        siteDictionary['form_weather_filter'] = form_weather_filter
        siteDictionary['form_animal_filter'] = form_animal_filter
        siteDictionary['form_animal_name'] = form_animal_name
        siteDictionary['form_species_name'] = form_species_name
        siteDictionary['form_sex'] = form_sex

    return render_to_response('export_animal.html', siteDictionary, context_instance=RequestContext(request))
