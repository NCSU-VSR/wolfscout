from django.utils.unittest.case import TestCase
from services.remoteCollar.collarFileTransmitter import CollarFileTransmitter

class CollarFileTransmitterTestCases(TestCase):

    def testCollarFileTransmitter_init(self):
        CollarFileTransmitter('GSM999999999.TXT')