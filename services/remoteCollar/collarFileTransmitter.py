"""
Uses requests library to send an http request to our server.
The request contains the file that was most recently changed
That's it folks
"""
import requests

class CollarFileTransmitter(object):
    """
    CollarFileTransmitter requires a filename to issue an instance of the class.
    It immediately starts sending the file based on the filename passed to it.
    """
    def __init__(self, filename):
        self.HOST = '152.14.104.35'
        self.URL = "http://152.14.104.35/collar_data_upload/"
        self.file = {"demofile.TXT": open(filename, 'rb')}
        requests.post(self.URL, files=file)