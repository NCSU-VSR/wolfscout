__author__ = 'chris'

import os
import glob
from apps.crawler.gpscollar.collar import CollarParser
from apps.crawler.gpscollar.models import Collar, CollarData
from apps.crawler.cronos.views import scrapeStations
from apps.crawler.gpscollar.views import *
PATH_TO_SAMPLE_DATA = "/opt/webapps/ncsu/wolfscout/sample_data/"

scrapeStations()
for infile in glob.glob( os.path.join(PATH_TO_SAMPLE_DATA, '*.TXT') ):
    cp = CollarParser(infile)
    cp.processCSVIntoDatabase()