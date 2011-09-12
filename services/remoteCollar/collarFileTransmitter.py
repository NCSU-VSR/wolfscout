# USAGE: python FileSender.py [file]
"""
Code Based on Content Found:
http://forums.devshed.com/python-programming-11/sending-a-file-using-sockets-129281.html
"""
import sys, socket

class CollarFileTransmitter(object):
    """
    CollarFileTransmitter requires a filename to issue an instance of the class.
    It immediately starts sending the file based on the filename passed to it.
    Very little error checking at the moment.
    """
    def __init__(self, filename):
        self.HOST = '152.14.104.35'
        self.CPORT = 9091
        self.MPORT = 9090
        self.filename = filename
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cs.connect((self.HOST, self.CPORT))
        cs.send("SEND " +self.filename)
        cs.close()

        self.ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ms.connect((self.HOST, self.MPORT))

        self.f = open(self.filename, "rb")
        self.data = self.f.read()
        self.f.close()

        self.ms.send(self.data)
        self.ms.close()