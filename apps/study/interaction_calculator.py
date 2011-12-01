from django.conf import settings
from apps.study.models import *
from apps.crawler.gpscollar.models import *
from geopy.distance import distance as geopy_distance
from django.contrib.gis.measure import Distance, D
from django.core.exceptions import ValidationError

def findInteractionFromDataPoint(sourceCollarDataPoint, distance=settings.DEFAULT_INTERACTION_DISTANCE, interactiongroup=None):
    if not distance:
        return distance
    list_of_data_points_to_search = CollarData.objects.exclude(collar=sourceCollarDataPoint.collar)
    list_of_data_points_to_search = list_of_data_points_to_search.filter(GMT_DATETIME=sourceCollarDataPoint.GMT_DATETIME)
    list_of_data_points_to_search = list_of_data_points_to_search.filter(LOCATION__distance_lte=(sourceCollarDataPoint.LOCATION, D(km=distance)))
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

def processInteractionGroups():
    interaction_groups = AnimalInteractionGroup.objects.all()
    for interaction_group in interaction_groups:
        data_points = CollarData.objects.all()
        for dp in data_points:
            if interaction_group.distance:
                findInteractionFromDataPoint(dp, distance=interaction_group.distance, interactiongroup=interaction_group)
            else:
                findInteractionFromDataPoint(dp, interactiongroup=interaction_group)
    return 1