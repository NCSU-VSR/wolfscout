#Global Imports
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from sys import *
#Local Imports
from wolfscout.apps.wildlife.models import *

class CollarParser(object):
    """
    CollarParser receives input from a textfile source.
    once the input arrives it is parsed and inserted into the DB using the models from
    wildlife.models


    Outline:
        1. Open A File
        2. Read File
        3. When reading parse each line into a list by space
        4. Propagate Model data from file contents (filename contains collarID)
        5. Close File
        6. Return
    """

    def createCollar(self, collarIDToCheck):
        """
        createCollarID first looks up the collar in the db
        to determine if the collar already exists.
        If the collar is not found, it is created.
        After identification or creation, the collar object is added to self.
        """
        try:
            self.collar = Collar.objects.get(collarID=collarIDToCheck)
        except ObjectDoesNotExist:
            #Create Collar
            self.collar = Collar()
            self.collar.collarID = collarIDToCheck
            self.collar.save()

    def createCollarData(self, lineContents):
        """
        createCollarData uses the contents of the current value of self.line
        to populate a data point for a specific collar. Once created the data
        if valid will be saved to the database.
        """
        newCollarDataPoint = CollarData()
        newCollarDataPoint.collar = self.collar

        #Big list of things there from the line:
        newCollarDataPoint.GMT_DATETIME = self.generateDateTimeFromList(lineContents[1],
                                                                        lineContents[2])
        newCollarDataPoint.LMT_DATETIME = self.generateDateTimeFromList(lineContents[3],
                                                                        lineContents[4])

        newCollarDataPoint.ECEF_X = lineContents[5]
        newCollarDataPoint.ECEF_Y = lineContents[6]
        newCollarDataPoint.ECEF_Z = lineContents[7]
        newCollarDataPoint.LATITUDE = lineContents[8]
        newCollarDataPoint.LONGITUDE = lineContents[9]
        newCollarDataPoint.HEIGHT = lineContents[10]
        newCollarDataPoint.DOP = lineContents[11]
        newCollarDataPoint.NAV = lineContents[12]
        newCollarDataPoint.VALIDATED = False
        newCollarDataPoint.SATS_USED = lineContents[14]
        newCollarDataPoint.CH1_SATID = lineContents[15]
        newCollarDataPoint.CH1_CN = lineContents[16]
        newCollarDataPoint.CH2_SATID = lineContents[17]
        newCollarDataPoint.CH2_CN = lineContents[18]
        newCollarDataPoint.CH3_SATID = lineContents[19]
        newCollarDataPoint.CH3_CN = lineContents[20]
        newCollarDataPoint.CH4_SATID = lineContents[21]
        newCollarDataPoint.CH4_CN = lineContents[22]
        newCollarDataPoint.CH5_SATID = lineContents[23]
        newCollarDataPoint.CH5_CN = lineContents[24]
        newCollarDataPoint.CH6_SATID = lineContents[25]
        newCollarDataPoint.CH6_CN = lineContents[26]
        newCollarDataPoint.CH7_SATID = lineContents[27]
        newCollarDataPoint.CH7_CN = lineContents[28]
        newCollarDataPoint.CH8_SATID = lineContents[29]
        newCollarDataPoint.CH8_CN = lineContents[30]
        newCollarDataPoint.CH9_SATID = lineContents[31]
        newCollarDataPoint.CH9_CN = lineContents[32]
        newCollarDataPoint.CH10_SATID = lineContents[33]
        newCollarDataPoint.CH10_CN = lineContents[34]
        newCollarDataPoint.CH11_SATID = lineContents[35]
        newCollarDataPoint.CH11_CN = lineContents[36]
        newCollarDataPoint.CH12_SATID = lineContents[37]
        newCollarDataPoint.CH12_CN = lineContents[38]
        newCollarDataPoint.MAIN_VOL = lineContents[39]
        newCollarDataPoint.BU_VOL = lineContents[40]
        newCollarDataPoint.TEMP = lineContents[41]
        newCollarDataPoint.REMARKS = lineContents[42]

        newCollarDataPoint.save()

    def generateDateTimeFromList(self, dateString, timeString):
        """
        generateDateTimeFromList takes in:
            dateString = day.month.year
            timestring = hour:min:second
        It then combines this input into a datetime object
        for django and python
        Upon completion it returns the new object
        """
        dateList = dateString.split('.')
        timeList = timeString.split(':')
        dateTimeObject = datetime(int(dateList[2]),int(dateList[1]),int(dateList[0]),
                                  int(timeList[0]),int(timeList[1]),int(timeList[2]))
        return dateTimeObject

    def lineParser(self):
        """
        lineParser a simple function call to split
        the contents of the line into a list based
        off of a space delimeter.
        From here more functions are called to build
        the django objects and save them.
        """
        if self.line:
            lineContents = self.line.split(' ')
            if "N/A" in lineContents:
                return 0
            self.createCollarData(lineContents)
        else:
            return 1

    def fileReader(self):
        """
        fileReader opens the file using a with statement
        that should handle the try catching blocks automatically
        After opening the file it reads it one line at a time
        Ending the process when the last line has been read and
        processed.
        """
        try:
            with open(self.filename, 'r') as file:
                for self.line in file:
                    self.lineParser()
        except IOError, err:
            return err
        return 0
        
    def extractCollarIDFromFilename(self, filename):
        """
        extractCollarIDFromFilename uses the filename that is passed into the object
        to determine what the correct collarID is. This requires removing
        any slashes and extensions first.
        Then the letters "GSM" are removed, finally the result
        is saved to the instance.

        Example:
        /BeanBagChairs/Sample/GSM30812.TXT becomes 30812
        """
        self.collarID = filename.split('/')[-1].split('.')[0][3:]

    def processCSVIntoDatabase(self):
        self.extractCollarIDFromFilename(self.filename)
        self.createCollar(self.collarID)
        self.line = ""
        self.fileReader()

    def __init__(self, filename):
        """
        Takes in a filename, calls reader.
        """
        self.filename = filename
        self.processCSVIntoDatabase()