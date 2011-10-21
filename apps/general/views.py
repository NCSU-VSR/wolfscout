### Django Imports ####
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.sitemaps import ping_google
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
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
    return render_to_response('index.html', siteDictionary, context_instance=RequestContext(request))
    
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
    return render_to_response('wildlife.html', siteDictionary, context_instance=RequestContext(request))
    
def getDictionary(request):
    siteDictionary = {}
    siteDictionary['request'] = request
    siteDictionary['STATIC_URL'] = settings.STATIC_URL
    return siteDictionary