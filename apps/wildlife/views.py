### Django Imports ####
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.sitemaps import ping_google
from django.conf import settings
### Global Imports ####
import datetime
### Views ####

def index(request):
    """
    index
    Description:
        Responsible for the homepage being rendered to the user.
    Parameters:
        request - the request object
    """
    dictionaryToPassToTemplate = {}
    dictionaryToPassToTemplate['STATIC_URL'] = settings.STATIC_URL
    print settings.STATIC_URL
    dictionaryToPassToTemplate['request'] = request
    return render_to_response('index.html', dictionaryToPassToTemplate)