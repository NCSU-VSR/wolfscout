### Standard Library Imports
from sys import *
import os
import shutil
import difflib
from datetime import datetime
### Django Imports
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import Point
### Project Imports
from apps.wildlife.models import *
from apps.crawler.cronos.views import *
from apps.study.interaction_calculator import *

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
    #invalidCollarId = "Invalid"
    #collarID = None
    #filePath = None

    def __init__(self, filePath):
        """
        Takes in a filename for which this CollarParser will represent
        """
        self.filePath = filePath
        try:
            self.collarID = self.extractCollarIDFromFilename()
            if not self.collarID:
                raise ValueError("The filename was not formatted properly, please submit a correct filename.")
        except ValueError:
            raise ValueError("The filename was not formatted properly, please submit a correct filename.")


    def createCollar(self):
        """
        Creates a collar in the db. If the collar already exists,
        then it will be overwritten.
        After identification or creation, the collar object is added to self.
        """
        self.collar = Collar()
        self.collar.collarID = self.collarID
        self.collar.save()

    def collarExists(self):
        """
        Returns the collar in the db if it exists.
        Else returns None
        """
        try:
            Collar.objects.get(collarID=self.collarID)
            return True
        except (ObjectDoesNotExist, ValueError):
            return False

    def stringToBool(self, string):
        """
        stringToBool takes in a string, in this case it must be
        Yes or No
        If the string is Yes: return True
        Else: return False
        """
        if string == "Yes":
            return True
        elif string == "No":
            return False
        else:
            raise ValueError("Invalid argument (must be Yes or No): {0}".format(string))

    def createCollarData(self, lineContents):
        """
        createCollarData uses the contents of the current value of self.line
        to populate a data point for a specific collar. Once created the data
        will be saved to the database. If the any of the data is found to be invalid,
        the 'VALID' flag will be set to False.
             """
        CSV = settings.CSV_DICTIONARY
        newCollarDataPoint = CollarData()
        newCollarDataPoint.collar = self.collar
        newCollarDataPoint.VALID = True
        #Big list of things there from the line:
        try:
            newCollarDataPoint.GMT_DATETIME = self.generateDateTimeFromList(lineContents[1],
                lineContents[2])
            newCollarDataPoint.LMT_DATETIME = self.generateDateTimeFromList(lineContents[3],
                lineContents[4])
        except ValueError:
            newCollarDataPoint.VALID = False
            return 0

        try:
            newCollarDataPoint.ECEF_X = lineContents[CSV['ECEF_X']]
            newCollarDataPoint.ECEF_Y = lineContents[CSV['ECEF_Y']]
            newCollarDataPoint.ECEF_Z = lineContents[CSV['ECEF_Z']]
            newCollarDataPoint.LATITUDE = lineContents[CSV['LATITUDE']]
            newCollarDataPoint.LONGITUDE = lineContents[CSV['LONGITUDE']]
            newCollarDataPoint.HEIGHT = lineContents[CSV['HEIGHT']]
            newCollarDataPoint.LOCATION = Point(float(lineContents[CSV['LATITUDE']]),float(lineContents[CSV['LONGITUDE']]),)
            newCollarDataPoint.DOP = lineContents[CSV['DOP']]
            newCollarDataPoint.NAV = lineContents[CSV['NAV']]
            newCollarDataPoint.VALIDATED = self.stringToBool(str(lineContents[CSV['VALIDATED']]))
            newCollarDataPoint.SATS_USED = lineContents[CSV['SATS_USED']]
            newCollarDataPoint.CH1_SATID = lineContents[CSV['CH1_SATID']]
            newCollarDataPoint.CH1_CN = lineContents[CSV['CH1_CN']]
            newCollarDataPoint.CH2_SATID = lineContents[CSV['CH2_SATID']]
            newCollarDataPoint.CH2_CN = lineContents[CSV['CH2_CN']]
            newCollarDataPoint.CH3_SATID = lineContents[CSV['CH3_SATID']]
            newCollarDataPoint.CH3_CN = lineContents[CSV['CH3_CN']]
            newCollarDataPoint.CH4_SATID = lineContents[CSV['CH4_SATID']]
            newCollarDataPoint.CH4_CN = lineContents[CSV['CH4_CN']]
            newCollarDataPoint.CH5_SATID = lineContents[CSV['CH5_SATID']]
            newCollarDataPoint.CH5_CN = lineContents[CSV['CH5_CN']]
            newCollarDataPoint.CH6_SATID = lineContents[CSV['CH6_SATID']]
            newCollarDataPoint.CH6_CN = lineContents[CSV['CH6_CN']]
            newCollarDataPoint.CH7_SATID = lineContents[CSV['CH7_SATID']]
            newCollarDataPoint.CH7_CN = lineContents[CSV['CH7_CN']]
            newCollarDataPoint.CH8_SATID = lineContents[CSV['CH8_SATID']]
            newCollarDataPoint.CH8_CN = lineContents[CSV['CH8_CN']]
            newCollarDataPoint.CH9_SATID = lineContents[CSV['CH9_SATID']]
            newCollarDataPoint.CH9_CN = lineContents[CSV['CH9_CN']]
            newCollarDataPoint.CH10_SATID = lineContents[CSV['CH10_SATID']]
            newCollarDataPoint.CH10_CN = lineContents[CSV['CH10_CN']]
            newCollarDataPoint.CH11_SATID = lineContents[CSV['CH11_SATID']]
            newCollarDataPoint.CH11_CN = lineContents[CSV['CH11_CN']]
            newCollarDataPoint.CH12_SATID = lineContents[CSV['CH12_SATID']]
            newCollarDataPoint.CH12_CN = lineContents[CSV['CH12_CN']]
            newCollarDataPoint.MAIN_VOL = lineContents[CSV['MAIN_VOL']]
            newCollarDataPoint.BU_VOL = lineContents[CSV['BU_VOL']]
            newCollarDataPoint.TEMP = lineContents[CSV['TEMP']]
            try:
                newCollarDataPoint.REMARKS = lineContents[CSV['REMARKS']]
            except IndexError:
                pass
        except IndexError:
            newCollarDataPoint.VALID = False
        try:
            #newCollarDataPoint.full_clean()
            newCollarDataPoint.weatherDataPoint = getWeatherData(newCollarDataPoint)
            newCollarDataPoint.save()
        except ValidationError:
            return
        #findInteractionFromDataPoint(newCollarDataPoint)


    def generateDateTimeFromList(self, dateString, timeString):
        """
        generateDateTimeFromList takes in:
            dateString = day.month.year
            timestring = hour:min:second
        It then combines this input into a datetime object
        for django and python
        Upon completion it returns the new object
        """
        if dateString is not None and timeString is not None:
            dateList = dateString.split('.')
            timeList = timeString.split(':')
            validArgs = len(dateList) == 3 and len(timeList) == 3 and dateString.find(" ") == -1 and timeString.find(" ") == -1
        else:
            validArgs = False
        if validArgs:
            dateTimeObject = datetime.datetime(int(dateList[2]),int(dateList[1]),int(dateList[0]), int(timeList[0]),int(timeList[1]),int(timeList[2]))
            if dateTimeObject > datetime.datetime.today():
                raise ValueError("Date is in the future. \nGiven date: {0}\nToday's date: {1}".format(dateTimeObject, datetime.datetime.today()))
            elif dateTimeObject.year < 1950:
                raise ValueError("Date is before the year 1950\nGiven date: {0}".format(dateTimeObject))

        else:
            raise ValueError("Invalid args\nDate String (day.month.year): '{0}'\nTime String (hour:min:second): '{1}'".format(dateString, timeString))

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
            new_file = open(self.filePath, 'r')
            existing_file_path = "/opt/webapps/ncsu/wolfscout/known_collar_data/"+"GSM"+str(self.collarID)+".TXT"
            if os.path.exists(existing_file_path):
                existing_file = open(existing_file_path, 'r')
                diffs = difflib.ndiff(existing_file.readlines(), new_file.readlines())
                for diff in diffs:
                    if diff[:2] == '+ ':
                        #print diff[2:]
                        self.line = diff[2:]
                        self.lineParser()
                new_file.close()
                existing_file.close()
            else:
                for self.line in new_file:
                    self.lineParser()
            shutil.copyfile(self.filePath, existing_file_path)
        except IOError, err:
            return err
        return 0

    def extractCollarIDFromFilename(self):
        """
        Returns the collar ID based on this collar parser's file name.
        extractCollarIDFromFilename uses the filename that is passed into the object
        to determine what the correct collarID is. This requires removing
        any slashes and extensions first.
        Then the letters "GSM" are removed, finally the result
        is saved to the instance.

        Example:
        /BeanBagChairs/Sample/GSM30812.TXT becomes 30812

        If the file name is malformed, the collar ID will be set to
        'Invalid'.
        """
        try:
            fileName = self.filePath.split('/')[-1]
            fileName = fileName.split("-")[-1]
            print "FileName: ", fileName
            if fileName.startswith('GSM') and fileName.endswith('.TXT'):
                collarID = fileName.split('.')[0][3:]
                if collarID.isdigit():
                    return collarID
        except:
            raise ValueError("The file must be a TXT file and the name must begin with 'GSM'" \
                             " followed by the collar ID which must be an number. For example, " \
                             "'GSM0005.TXT'\nFile name: {0}".format(self.filePath))

    def processCSVIntoDatabase(self):
        """
        processCSVIntoDatabase issues the functions listed below in linear order.
        This places all of the data from a CSV into the database unless an error is found
        """
        if not self.collarID:
            return 0
        elif self.collarExists() == False:
            self.createCollar()
        else:
            self.collar = Collar.objects.get(pk=self.collarID)
        self.line = ""
        self.fileReader()