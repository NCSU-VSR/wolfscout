### Django Imports ####
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.sitemaps import ping_google
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
### Global Imports ####
import datetime
### Local Imports ###
from apps.wildlife.models import Collar
from apps.wildlife.models import CollarData
from apps.general.views import getDictionary

### Views ####

def getCollars(request):
    """
    createCollarID first looks up the collar in the db
    to determine if the collar already exists.
    If the collar is not found, it is created.
    After identification or creation, the collar object is added to self.
    """
    collars = Collar.objects.all()
    siteDictionary = getDictionary(request)
    siteDictionary['collars']=collars
    return render_to_response('collars_test.html', siteDictionary)

def getCollarData(request):
    """
    """
    collarData = CollarData.objects.all()
    collars = Collar.objects.all()
    siteDictionary = getDictionary(request)
    siteDictionary['collarData']=collarData
    siteDictionary['collars']=collars
    return render_to_response('collars_test.html', siteDictionary)
