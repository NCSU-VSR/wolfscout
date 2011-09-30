### Django Imports ####
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.sitemaps import ping_google
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
### Global Imports ####
import datetime
### Views ####

@login_required()
def index(request):
    """
    index
    Description:
        Responsible for the login being rendered to the user.
    Parameters:
        request - the request object
    """
    siteDictionary = getDictionary(request)
    print str(request.path)
    return render_to_response('index.html', siteDictionary)
    
@login_required()
def wildlife(request):
    """
    index
    Description:
        Responsible for the login being rendered to the user.
    Parameters:
        request - the request object
    """
    siteDictionary = getDictionary(request)
    return render_to_response('wildlife.html', siteDictionary)
    
def getDictionary(request):
    siteDictionary = {}
    siteDictionary['request'] = request
    siteDictionary['STATIC_URL'] = settings.STATIC_URL
    return siteDictionary
