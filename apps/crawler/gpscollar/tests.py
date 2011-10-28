"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from apps.crawler.gpscollar.collar import *
from sys import *

class CollarTestCases(TestCase):
    validCollarID = "30812"
    validFileName = "sample_data/GSM30812.TXT"
    invalidCollarID = "999999999"

    def test_setting_filename_at_init(self):
        filename = "theHappyCat.txt"
        testCollarParser = CollarParser(filename)
        self.assertEquals(testCollarParser.filename,filename)

    def test_collarExists_true(self):
        collarID = CollarTestCases.validCollarID
        testCollarParser = self.getTestCollarParser()
        testCollarParser.createCollar(collarID)
        self.assertTrue(testCollarParser.collarExists(collarID))

    def test_collarExists_false(self):
        invalidCollarID = CollarTestCases.invalidCollarID
        testCollarParser = self.getTestCollarParser()
        self.assertFalse(testCollarParser.collarExists(invalidCollarID))

    def test_collarExists_badInput(self):
        badInput = "badInput9999"
        testCollarParser = self.getTestCollarParser()
        try:
            testCollarParser.collarExists(badInput)
            self.fail()
        except ValueError:
            pass

    def test_stringToBool_true(self):
        string = "Yes"
        testCollarParser = self.getTestCollarParser()
        self.assertTrue(testCollarParser.stringToBool(string))

    def test_stringToBool_false(self):
        string = "No"
        testCollarParser = self.getTestCollarParser()
        self.assertFalse(testCollarParser.stringToBool(string))

    def test_stringToBool_badInput(self):
        string = "abbadabba"
        testCollarParser = self.getTestCollarParser()
        try:
            testCollarParser.stringToBool(string)
            self.fail()
        except:
            pass

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
            pass
        #TODO Is this how we want to handle this?


    def test_fileReaderWithBadFile(self):
        badFilename = "thisfileneverexists.txt"
        noFileIOError = IOError(2, 'No such file or directory')
        testCollarParser = CollarParser(badFilename)
        self.assertEquals(testCollarParser.fileReader().args[1],noFileIOError.args[1])

    def test_generateDateTimeFromList_validInput(self):
        validDateString = "28.2.2011"
        validTimeString = "0:0:0"
        testCollarParser = self.getTestCollarParser()
        testCollarParser.generateDateTimeFromList(validDateString, validTimeString)

    def test_generateDateTimeFromList_badDate(self):
        testCollarParser = self.getTestCollarParser()
        for badDate in self.getBadDateStrings():
            try:
                testCollarParser.generateDateTimeFromList(badDate, self.getValidTimeString())
                self.fail(badDate)
            except ValueError:
                pass
            except AttributeError:
                if badDate != None:
                    raise

    def test_generateDateTimeFromList_badTime(self):
        testCollarParser = self.getTestCollarParser()
        for badTime in self.getBadTimeStrings():
            try:
                testCollarParser.generateDateTimeFromList(self.getValidDateString(), badTime)
                self.fail(badTime)
            except ValueError:
                pass
            except AttributeError:
                if badTime != None:
                    raise

    def getTestCollarParser(self):
        return CollarParser(self.validFileName)

    def getValidDateString(self):
        return "28.2.2011"

    def getValidTimeString(self):
        return "0:0:0"

    def getBadDateStrings(self):
        return (None, "-1.1.2011", "29.2.2011", "31.4.2011", "0.1.2011", "a.1.2011", "1a.1.2011", "one.1.2011", ".1.2011", "1 .1.2011",
            "1.-1.2011", "1.0.2011", "1.13.2011", "1.1a.2011", "1.a.2011", "1.one.2011", "1..2011", "1. 1.2011",
            "1.1.-1", "1.1.2025", "1.1.500", "1.1.0", "1.1.2011a", "1.1.201a", "1.1.a", "1.1.twozerooneone", "1.1.", "1.1. 2011",
            "1.1.2011.", ".1.1.2011", "1 1 2011", "1 1.2011", "1,1.2011", "1:1.2011", "1,1,2011", "1:1:2011")

    def getBadTimeStrings(self):
        return (None, "-1:1:1", "24:1:1", "1a:1:1", "a:1:1", ":1:1", "1 :1:1",
            "1:-1:1" "1:60:1", "1:1a:1", "1:a:1", "1::1", "1:1 :1",
            "1:1:-1", "1:1:60", "1:1:1a", "1:1:a", "1:1:", "1:1:1 ",
            "1:1:1:", ":1:1:1", "1 1 1", "1 1:1", "1,1:1", "1.1:1", "1,1,1", "1.1.1")