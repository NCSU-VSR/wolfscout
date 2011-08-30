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

    def createCollarID(self):
        """
        createCollarID first looks up the collar in the db
        to determine if the collar already exists.
        If the collar is not found, it is created.
        After identification or creation, the collar object is added to self.
        """
        collarID = Collar.objects.get(collar_ID==self.collarID)
        if collarID is not None:
            print collarID
        return 0

    def lineParser(self):
        """
        lineParser a simple function call to split
        the contents of the line into a list based
        off of a space delimeter.
        From here more functions are called to build
        the django objects and save them.
        """
        if self.line:
            self.lineContents = self.line.split(' ')
            print self.lineContents
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
        with open(self.filename, 'r') as file:
            for self.line in file:
                self.lineParser()
        return 0
        

    def __init__(self, filename):
        """
        Takes in a filename, calls reader.
        """
        self.filename= filename
        self.fileReader()
        self.line = None
