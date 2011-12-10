### Standard Library Imports
import os
import glob
### Django Imports

### Project Imports
from apps.crawler.gpscollar.collar import CollarParser
from apps.crawler.gpscollar.models import Collar, CollarData
from apps.crawler.cronos.views import scrapeStations
from apps.crawler.gpscollar.views import *


"""
Usage:
python apps/crawler/gpscollar/fileProcessor.py
"""


#This is the path to all of the known data points we collected.
PATH_TO_SAMPLE_DATA = "/opt/webapps/ncsu/wolfscout/sample_data/"

#Scrape stations will build an index of all the known weather stations
scrapeStations()

#This loop is used to grab all the .TXT files and then process them through collar.py
for infile in glob.glob( os.path.join(PATH_TO_SAMPLE_DATA, '*.TXT') ):
    cp = CollarParser(infile)
    cp.processCSVIntoDatabase()