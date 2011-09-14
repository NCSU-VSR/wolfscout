"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from apps.crawler.collar import *
from sys import *

class CollarTestCases(TestCase):
    validCollarID = "30812"
    validFileName = "sample_data/GSM30812.TXT"
    invalidCollarID = "999999999"

    def test_setting_filename_at_init(self):
        filename = "theHappyCat.txt"
        testCollarParser = CollarParser(filename)
        self.assertEquals(testCollarParser.filename,filename)

    def test_collarExists_True(self):
        collarID = CollarTestCases.validCollarID
        testCollarParser = self.getTestCollarParser()
        testCollarParser.createCollar(collarID)
        self.assertTrue(testCollarParser.collarExists(collarID))

    def text_collarExists_False(self):
        invalidCollarID = CollarTestCases.invalidCollarID
        testCollarParser = self.getTestCollarParser()
        self.assertFalse(testCollarParser.collarExists(invalidCollarID))

    def text_collarExists_BadInput(self):
        badInput = "badInput9999"
        testCollarParser = self.getTestCollarParser()
        self.assertFalse(testCollarParser.collarExists(badInput))

    def test_extractCollarIDFromFilename_validFileName(self):
        collarID = CollarTestCases.validCollarID
        fileName = CollarTestCases.validFileName
        testCollarParser = CollarParser(fileName)
        testCollarParser.extractCollarIDFromFilename(testCollarParser.filename)
        self.assertEquals(testCollarParser.collarID,collarID)

    def test_extractCollarIDFromFilename_invalidFilename(self):
        """
        Tests extracting a collar ID from a malformed filename
        """""
        collarID = self.validCollarID
        badFileNames = ["sample_data/GS{0}.TXT".format(collarID), "sample_data/GSM{0}.TX".format(collarID)]
        for badFileName in badFileNames:
            testCollarParser = CollarParser(badFileName)
            testCollarParser.extractCollarIDFromFilename(testCollarParser.filename)
            self.assertEquals(testCollarParser.collarID,CollarParser.invalidCollarId)

    def test_createCollar(self):
        testcollarID = "3082225"
        testCollarParser = CollarParser("sample_data/GSM30812.TXT")
        testCollarParser.createCollar(testcollarID)
        newCollarToCheckFor = Collar.objects.get(collarID=testcollarID)
        self.assertEquals(newCollarToCheckFor.collarID,int(testcollarID))

    def test_createCollar_badCollarID(self):
        testCollarID = "badCollarID9999"
        testCollarParser = self.getTestCollarParser()
        try:
            testCollarParser.createCollar(testCollarID)
            self.fail()
        except ValueError:
            return
        #TODO Is this how we want to handle this?


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

    def getTestCollarParser(self):
        return CollarParser(self.validFileName)