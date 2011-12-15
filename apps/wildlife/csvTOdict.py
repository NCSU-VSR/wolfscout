__author__ = 'laurencharles-smith'

# Create file that reads csv data, parses the data into a list and adds to dictionary

##Creates a DictReader object which can parse the given file, returning a #dictionary of values for each line of the file.
# The dictionary keys are #typically the first line of the file. You can, optionally, provide the field #names if
# they are not the first line of the file. The csvfile can be any #iterable object.

import csv

infile = open ('/opt/webapps/ncsu/wolfscout/sample_data/coyote-demographics.csv','rU')

dem = csv.DictReader(infile)

#for row in dem:
#        print row

#for data in dem:
#    print data["Trap"]

infile.close()