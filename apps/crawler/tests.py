"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from apps.crawler.collar import *
from sys import *

class CollarTestCases(TestCase):

    def test_setting_filename_at_init(self):
        filename = "theHappyCat.txt"
        testCollarParser = CollarParser(filename)
        self.assertEquals(testCollarParser.filename,filename)

    def test_extractCollarIDFromFilename(self):
        collarID = "30812"
        testCollarParser = CollarParser("sample_data/GSM30812.TXT")
        testCollarParser.extractCollarIDFromFilename(testCollarParser.filename)
        self.assertEquals(testCollarParser.collarID,collarID)

    def test_createCollar(self):
        testcollarID = "3082225"
        testCollarParser = CollarParser("sample_data/GSM30812.TXT")
        testCollarParser.createCollar(testcollarID)
        newCollarToCheckFor = Collar.objects.get(collarID=testcollarID)
        self.assertEquals(newCollarToCheckFor.collarID,int(testcollarID))

    def test_fileReaderWithBadFile(self):
        badFilename = "thisfileneverexists.txt"
        noFileIOError = IOError(2, 'No such file or directory')
        testCollarParser = CollarParser(badFilename)
        self.assertEquals(testCollarParser.fileReader().args[1],noFileIOError.args[1])

    def test_generateDateTimeFromList(self):
        dateString = "12.1.2011"
        timeString = "1:25:10"
        dateList = dateString.split('.')
        timeList = timeString.split(':')
        dateTimeObjectToTest = datetime(int(dateList[2]),int(dateList[1]),int(dateList[0]),
                                  int(timeList[0]),int(timeList[1]),int(timeList[2]))
        testCollarParser = CollarParser("fred")
        self.assertEqual(testCollarParser.generateDateTimeFromList(dateString,timeString),dateTimeObjectToTest)

    