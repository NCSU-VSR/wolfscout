__author__ = 'chris'
from django.contrib.gis.measure import Distance, D
from geopy.distance import distance as geopy_distance
from apps.crawler.gpscollar.models import Collar, CollarData

#### Static Vars ####

DISTANCE_TO_SEARCH = .05

def findAllMatchingByDistance(sourceCollar, distance=None):
    if not distance:
        return distance
    sourceCollarDataPoints = CollarData.objects.filter(collar=sourceCollar)
    matches = CollarData.objects.exclude(collar=sourceCollar)
    for sourceDataPoint in sourceCollarDataPoints:
        thesematches = matches.filter(GMT_DATETIME=sourceDataPoint.GMT_DATETIME)
        thesematches = thesematches.filter(LOCATION__distance_lte=(sourceDataPoint.LOCATION, D(km=distance)))
        #aftermatches = matches.filter(GMT_DATETIME__gt=sourceDataPoint.GMT_DATETIME)

        if len(thesematches) > 0:
            print "Collar: " + str(sourceDataPoint.collar.collarID)
            print "Source Data Point: " + str(sourceDataPoint.pk)
            print "Exact Matches: " + str(sourceDataPoint.GMT_DATETIME)
            for i,match in enumerate(thesematches):
                print "match: " + str(i+1)  + " CollarID: " + str(match.collar.collarID) +\
                      " , CollarDataPointID: " + str(match.pk)
                print "Distance from source was: " + str(geopy_distance(sourceDataPoint.LOCATION,match.LOCATION))


def processAllCollars():
    collars = Collar.objects.all()
    for collar in collars:
        findAllMatchingByDistance(collar.collarID, DISTANCE_TO_SEARCH)

processAllCollars()