### Standard Library Imports
from sys import *
import datetime
### Django Imports
from django.conf import settings
from geopy.distance import distance as geopy_distance
from django.contrib.gis.measure import Distance, D
from django.core.exceptions import ValidationError
### Project Imports
from apps.study.models import *
from apps.crawler.gpscollar.models import *
from apps.crawler.gpscollar.views import *
from django.core.files.base import ContentFile

def findInteractionFromDataPoint(sourceCollarDataPoint, distance=settings.DEFAULT_INTERACTION_DISTANCE, timedelta=None, starttime=None, endtime=None, interactiongroup=None):
    list_of_data_points_to_search = CollarData.objects.exclude(collar=sourceCollarDataPoint.collar)
    if starttime:
        if endtime:
            list_of_data_points_to_search = list_of_data_points_to_search.filter(GMT_DATETIME__range=(starttime, endtime))
        else:
            list_of_data_points_to_search = list_of_data_points_to_search.filter(GMT_DATETIME__gte=starttime)
    elif endtime:
        list_of_data_points_to_search = list_of_data_points_to_search.filter(GMT_DATETIME__lte=endtime)
    if distance:
        list_of_data_points_to_search = list_of_data_points_to_search.filter(LOCATION__distance_lte=(sourceCollarDataPoint.LOCATION, D(km=distance)))
    if timedelta:
        real_time_delta = datetime.timedelta(seconds=timedelta)
        start_delta = sourceCollarDataPoint.GMT_DATETIME - real_time_delta
        end_delta = sourceCollarDataPoint.GMT_DATETIME + real_time_delta
        list_of_data_points_to_search = list_of_data_points_to_search.filter(GMT_DATETIME__range=(start_delta, end_delta))
    else:
        list_of_data_points_to_search = list_of_data_points_to_search.filter(GMT_DATETIME=sourceCollarDataPoint.GMT_DATETIME)
    for match in list_of_data_points_to_search:
        animal_interaction_to_add = AnimalInteraction()
        animal_interaction_to_add.source_animal_data_point = sourceCollarDataPoint
        animal_interaction_to_add.destination_animal_data_point = match
        animal_interaction_to_add.distance = geopy_distance(sourceCollarDataPoint.LOCATION,match.LOCATION).kilometers
        animal_interaction_to_add.interaction_group = interactiongroup
        try:
            animal_interaction_to_add.clean()
            animal_interaction_to_add.save()
        except ValidationError:
            print "The entry already exists"
    zip_content = ContentFile(exportShape())
    interactiongroup.zip_file.save("sampleFile.zip",zip_content)
    interactiongroup.save()

def processAnimalInteractionGroups():
    interaction_groups = AnimalInteractionGroup.objects.all()
    for interaction_group in interaction_groups:
        data_points = CollarData.objects.all()
        for dp in data_points:
            if interaction_group.distance:
                findInteractionFromDataPoint(sourceCollarDataPoint=dp, distance=interaction_group.distance,
                    timedelta=interaction_group.time_delta, starttime=interaction_group.start_time,
                    endtime=interaction_group.end_time, interactiongroup=interaction_group)
            else:
                findInteractionFromDataPoint(sourceCollarDataPoint=dp, timedelta=interaction_group.time_delta, starttime=interaction_group.start_time,
                    endtime=interaction_group.end_time, interactiongroup=interaction_group)

def findInteractionDataFromShapes(sourceShape, sourceCollarDataPoint, distance=settings.DEFAULT_INTERACTION_DISTANCE, timedelta=None, starttime=None, endtime=None, interactiongroup=None):
    list_of_data_points_to_search = CollarData.objects.all()
    if starttime:
        if endtime:
            list_of_data_points_to_search = list_of_data_points_to_search.filter(GMT_DATETIME__range=(starttime, endtime))
        else:
            list_of_data_points_to_search = list_of_data_points_to_search.filter(GMT_DATETIME__gte=starttime)
    elif endtime:
        list_of_data_points_to_search = list_of_data_points_to_search.filter(GMT_DATETIME__lte=endtime)
    if distance:
        list_of_data_points_to_search = list_of_data_points_to_search.filter(LOCATION__distance_lte=(sourceShape.shape, D(km=distance)))
    if timedelta:
        real_time_delta = datetime.timedelta(seconds=timedelta)
        start_delta = sourceCollarDataPoint.GMT_DATETIME - real_time_delta
        end_delta = sourceCollarDataPoint.GMT_DATETIME + real_time_delta
        list_of_data_points_to_search = list_of_data_points_to_search.filter(GMT_DATETIME__range=(start_delta, end_delta))
    for match in list_of_data_points_to_search:
        shape_interaction_to_add = ShapeInteraction()
        shape_interaction_to_add.source_shapes = sourceShape
        shape_interaction_to_add.destination_animal_data_point = match
        shape_interaction_to_add.distance = geopy_distance(sourceShape.shape,match.LOCATION).kilometers
        shape_interaction_to_add.interaction_group = interactiongroup
        shape_interaction_to_add.date_time = match.GMT_DATETIME
        try:
            shape_interaction_to_add.clean()
            shape_interaction_to_add.save()
        except ValidationError:
            print "The entry already exists"
    zip_content = ContentFile(exportShape())
    interactiongroup.zip_file.save("sampleFile.zip",zip_content)
    interactiongroup.save()

def processShapeInteractionGroups():
    interaction_groups = ShapeInteractionGroup.objects.all()
    for interaction_group in interaction_groups:
        data_points = ShapeToAnalyze.objects.all()
        for dp in data_points:
            if interaction_group.distance:
                findInteractionDataFromShapes(sourceShape=dp, distance=interaction_group.distance,
                    timedelta=interaction_group.time_delta, starttime=interaction_group.start_time,
                    endtime=interaction_group.end_time, interactiongroup=interaction_group)
            else:
                findInteractionDataFromShapes(sourceShape=dp, timedelta=interaction_group.time_delta, starttime=interaction_group.start_time,
                    endtime=interaction_group.end_time, interactiongroup=interaction_group)