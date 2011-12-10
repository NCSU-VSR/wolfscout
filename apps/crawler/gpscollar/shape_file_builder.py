

import shapefile
from apps.crawler.gpscollar.models import  *
from apps.crawler.cronos.models import *
filename = "/Users/chris/sample/demofile"
#import shapefile as sf

w = shapefile.Writer(shapefile.POINT)
w.autoBalance = 1


w.field("CollarID")
w.field("LMT_DATETIME")
w.field("TEMP")
w.field("WeatherDataPoint")
w.field("Station Code")
w.field("Location")
w.field("Station Name")
datapoints = CollarData.objects.all()
for point in datapoints:
    w.point(point.LOCATION.x, point.LOCATION.y)
    w.record(point.collar, point.LMT_DATETIME,point.TEMP, point.weatherDataPoint, point.weatherDataPoint.station.station_code,
        point.weatherDataPoint.station.LOCATION, point.weatherDataPoint.station.name)
#w.record(cdp.collar,cdp.LMT_DATETIME,cdp.TEMP,cdp.weatherDataPoint)
print "location: ", w.shapes()[0].points
w.save(filename)


"""
#filename = 'test/point'

# create the shapefile
w = sf.Writer(sf.POINT)
cdp = CollarData.objects.all()[1200]
w.point(cdp.LOCATION.y, cdp.LOCATION.x)
#w.point(37.7793, -122.4192)
w.field('FIRST_FLD')
w.record('First','Point')
w.save(filename)
print "location: ", w.shapes()[0].points

# create the PRJ file
prj = open("%s.prj" % filename, "w")
epsg = 'PROJCS["NAD_1983_UTM_Zone_17N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137,298.257222101]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000],PARAMETER["False_Northing",0],PARAMETER["Central_Meridian",-81],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0],UNIT["Meter",1]]'
prj.write(epsg)
prj.close()
"""