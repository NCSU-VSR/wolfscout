__author__ = 'sagentry'

### Django Imports ####
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
### Global Imports ####
import csv
### Local Imports ###
from apps.wildlife.forms import *
from apps.crawler.gpscollar.support import *
from apps.crawler.cronos.models import *
from apps.general.forms import *
from apps.general.views import *
from settings.common import CLIMATE_DICTIONARY

def getCSV(form_animal_name, form_species_name, form_sex, form_age, form_collars_filter, form_weather_filter):
    """
    Returns a created CSV of the selected animals demographic infromation, including the collar and weather information
    selected with the collar/weather filter checkboxes in the DOM
    """
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=ExportByAnimal.csv'

    writer = csv.writer(response)

    writer = writeHeaders(writer, form_collars_filter, form_weather_filter)

    if(isAnimalSelected(form_animal_name)):
        writer = filterByAnimal(writer, form_animal_name, form_collars_filter, form_weather_filter)
    else:
        print "Filtering by anything other than specific animals is not currently implemented"
        #writer = filterByEverythingElse(writer, form_species_name, form_sex, form_collars_filter, form_weather_filter, isSpeciesSelected(form_species_name), isSexSelected(form_sex))

    return response

def filterByEverythingElse(writer, form_species_name, form_sex, form_collars_filter, form_weather_filter, isSpeciesSelected, isSexSelected):
    """
    Attempts to filter by age, sex, time, date, species - but is not current working.  Have at it.
    """
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

def filterByAnimal(writer, form_animal_name, form_collars_filter, form_weather_filter):
    """
    Returns the writer for the CSV of the selected Animal(s) in the DOM.  Only filter options considered
    are those selected in the collar/weather filters and animals selected in the DOM
    """
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
            headerList.append(CLIMATE_DICTIONARY[field.name][0] + " " + CLIMATE_DICTIONARY[field.name][1])
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

def isAgeSelected(form_age):
    """
    Checks to see if age is selected in the DOM
    """
    for field in Animal.AGE_CHOICES:
        if form_age.cleaned_data[str(field[0])]:
            return True
    return False

def export(request):
    """
    Export method of the export_animal template.  Currently, only exports CSVs based on the selected animals, not including
    sex, species, time, date, and age at this point.  The template, however, is set up for completion of this functionality.
    Uncomment all the information in the template that has been commented out.  The Javascript related to the UI logic should
    already be enabled and working.  If there are issues, it is located under static/js/wolfscout.js.  Those forms are implemented
    within this method for sex, date, time, etc - but need methods (like the ones started above) to finish implementation.
    """
    siteDictionary = getDictionary(request)
    if request.method == 'POST':
        form_collars_filter = ExportCollarDataFilterForm(request.POST, error_class=DivErrorList)
        form_weather_filter = ExportWeatherDataFilterForm(request.POST, error_class=DivErrorList)
        form_animal_filter = ExportAnimalFilterForm(request.POST, error_class=DivErrorList)
        form_animal_name = AnimalByNameForm(request.POST, error_class=DivErrorList, auto_id='id_animal_%s')
        form_species_name = SpeciesByNameForm(request.POST, error_class=DivErrorList, auto_id='id_species_%s')
        form_sex = SexForm(request.POST, error_class=DivErrorList)
        form_age = AgeForm(request.POST, error_class=DivErrorList)
        form_export_animal_type = ExportAnimalTypeForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        if form_animal_name.is_valid() and form_species_name.is_valid() and form_sex.is_valid() and form_collars_filter.is_valid() and form_weather_filter.is_valid() and form_animal_filter.is_valid() and form_export_animal_type.is_valid() and form_age.is_valid():
            is_csv = form_export_animal_type.cleaned_data['is_csv']
            is_shape = form_export_animal_type.cleaned_data['is_shape']
            if is_csv:
                return getCSV(form_animal_name, form_species_name, form_sex, form_age, form_collars_filter, form_weather_filter)
            if is_shape:
                print "Shape export functionality current not implemented"
    else:
        animals = Animal.objects.all()
        species = Species.objects.all()
        form_collars_filter = ExportCollarDataFilterForm(auto_id='id_collar_filter_%s')
        form_weather_filter = ExportWeatherDataFilterForm(auto_id='id_weather_filter_%s')
        form_animal_filter = ExportAnimalFilterForm(auto_id='id_animal_filter_%s')
        form_animal_name = AnimalByNameForm(auto_id='id_animal_%s')
        form_species_name = SpeciesByNameForm(auto_id='id_species_%s')
        form_sex = SexForm(auto_id='id_sex_%s')
        form_age = AgeForm(auto_id='id_age_%s')
        form_export_animal_type = ExportAnimalTypeForm(auto_id='id_%s')
        siteDictionary['animals'] = animals
        siteDictionary['species'] = species
        siteDictionary['form_collars_filter'] = form_collars_filter
        siteDictionary['form_weather_filter'] = form_weather_filter
        siteDictionary['form_animal_filter'] = form_animal_filter
        siteDictionary['form_animal_name'] = form_animal_name
        siteDictionary['form_species_name'] = form_species_name
        siteDictionary['form_sex'] = form_sex
        siteDictionary['form_age'] = form_age
        siteDictionary['form_export_animal_type'] = form_export_animal_type
    return render_to_response('export_animal.html', siteDictionary, context_instance=RequestContext(request))
