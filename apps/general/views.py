### Django Imports ####
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.sitemaps import ping_google
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
### Global Imports ####
import datetime
### Local Imports ####
from apps.study.models import Study
### Views ####

@login_required()
def index(request):
    """
    Renders our base index page
    """
    siteDictionary = getDictionary(request)
    return render_to_response('index.html', siteDictionary, context_instance=RequestContext(request))

def getDictionary(request):
    """
    Returns common dictionary elements used by multiple views
    """
    siteDictionary = {}
    siteDictionary['request'] = request
    siteDictionary['STATIC_URL'] = settings.STATIC_URL
    ### Required data for all pages ###
    myStudies = Study.objects.all().filter(owner=request.user) ### Creates object
    siteDictionary['myStudies']=myStudies
    siteDictionary['allStudies'] = Study.objects.all()
    return siteDictionary