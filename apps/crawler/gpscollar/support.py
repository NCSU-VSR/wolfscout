
from django.contrib.gis.measure import Distance, D
from apps.crawler.gpscollar.models import Collar, CollarData
from geopy.distance import distance as geopy_distance
#### Static Vars ####

DISTANCE_TO_SEARCH = .05

def findAllMatchingByDistance(sourceCollar, distance=None):
    if not distance:
        return distance
    sourceCollarDataPoints = CollarData.objects.filter(collar=sourceCollar)
    matches = CollarData.objects.exclude(collar=sourceCollar)
    matchesToReport = []
    for sourceDataPoint in sourceCollarDataPoints:
        thesematches = matches.filter(GMT_DATETIME=sourceDataPoint.GMT_DATETIME)
        thesematches = thesematches.filter(LOCATION__distance_lte=(sourceDataPoint.LOCATION, D(km=distance)))
        if len(thesematches) > 0:
            for i,match in enumerate(thesematches):
                thisMatch = Collar()
                thisMatch.sourceCollarID = sourceDataPoint.collar.collarID
                thisMatch.matchedCollarID = match.collar.collarID
                thisMatch.datetime = sourceDataPoint.GMT_DATETIME
                thisMatch.locationX = sourceDataPoint.LOCATION.x
                thisMatch.locationY = sourceDataPoint.LOCATION.y
                thisMatch.distance = str(geopy_distance(sourceDataPoint.LOCATION,match.LOCATION))
                matchesToReport.append(thisMatch)
    return matchesToReport

def processAllCollars():
    collars = Collar.objects.all()
    matches = []
    for collar in collars:
        matches += findAllMatchingByDistance(collar.collarID, DISTANCE_TO_SEARCH)
    return matches