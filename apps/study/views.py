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
from apps.general.views import getDictionary
from apps.study.models import Study
from apps.study.forms import EditStudyForm
from apps.study.forms import AddStudyForm
from apps.study.forms import DivErrorList
### Views ####

@login_required()
def studies(request):
    """
    """
    siteDictionary = getDictionary(request)
    return render_to_response('studies.html', siteDictionary, context_instance=RequestContext(request))
  
@login_required()  
def study(request, theStudyID):
    """
    """
    study = get_object_or_404(Study, pk=theStudyID)
    siteDictionary = getDictionary(request)
    siteDictionary['study'] = study
    return render_to_response('study.html', siteDictionary, context_instance=RequestContext(request))
        
@login_required()  
def edit(request, theStudyID):
    """
    """
    study = get_object_or_404(Study, pk=theStudyID)
    if request.method == 'POST':
        form = EditStudyForm(error_class=DivErrorList, auto_id='id_%s', instance=study)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('studies.html')
    else:
        form = EditStudyForm()
    return render_to_response('editStudy.html', {'form': form,}, context_instance=RequestContext(request))
    
@login_required()  
def add(request):
    """
    """
    if request.method == 'POST':
        form = AddStudyForm(error_class=DivErrorList, auto_id='id_%s', instance=Study)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('studies.html')
    else:
        form = AddStudyForm()
    return render_to_response('addStudy.html', {'form': form,}, context_instance=RequestContext(request))