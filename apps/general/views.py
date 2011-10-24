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
from apps.study.models import Experiment
### Views ####

@login_required()
def index(request):
    """
    """
    siteDictionary = getDictionary(request)
    return render_to_response('index.html', siteDictionary, context_instance=RequestContext(request))
    
@login_required()
def experiments(request):
    """
    """
    siteDictionary = getDictionary(request)
    return render_to_response('experiments.html', siteDictionary, context_instance=RequestContext(request))
  
@login_required()  
def experiment(request, theExperimentID):
    """
    """
    experiment = get_object_or_404(Experiment, pk=theExperimentID)
    siteDictionary = getDictionary(request)
    siteDictionary['experiment'] = experiment
    return render_to_response('experiment.html', siteDictionary, context_instance=RequestContext(request))
    
def getDictionary(request):
    siteDictionary = {}
    siteDictionary['request'] = request
    siteDictionary['STATIC_URL'] = settings.STATIC_URL
    ### Required data for all pages ###
    myExperiments = Experiment.objects.all().filter(owner=request.user) ### Creates object
    siteDictionary['myExperiments']=myExperiments ### Associates dictionary field with object to be called in html
    return siteDictionary