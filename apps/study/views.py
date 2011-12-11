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
from apps.study.models import *
from apps.study.forms import *
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
    siteDictionary = {}
    siteDictionary['title'] = "Edit Study"
    study = get_object_or_404(Study, pk=theStudyID)
    if request.method == 'POST':
        form = StudyForm(request.POST, error_class=DivErrorList, instance=Study.objects.get(pk=theStudyID))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/studies')
    else:
        form = StudyForm(error_class=DivErrorList, auto_id='id_%s', instance=study)
    siteDictionary['form'] = form
    return render_to_response('study_edit.html', siteDictionary, context_instance=RequestContext(request))

@login_required()  
def delete(request, theStudyID):
    """
    """
    siteDictionary = {}
    siteDictionary['title'] = "Delete Study"
    study = get_object_or_404(Study, pk=theStudyID)
    siteDictionary['study'] = study
    if request.method == 'POST':
        study.delete()
        return HttpResponseRedirect('/studies')
    return render_to_response('study_delete.html', siteDictionary, context_instance=RequestContext(request))   
    
@login_required()  
def add(request):
    """
    """
    siteDictionary = {}
    siteDictionary['title'] = "Add Study"
    if request.method == 'POST':
        form = StudyForm(request.POST, error_class=DivErrorList)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/studies')
    else:
        form = StudyForm(auto_id='id_%s', initial={'owner':request.user})
    siteDictionary['form'] = form
    return render_to_response('study_add.html', siteDictionary, context_instance=RequestContext(request))

@login_required()
def interactions(request):
    siteDictionary = getDictionary(request)
    siteDictionary['studies'] = Study.objects.all()
    return render_to_response('export_interactions.html', siteDictionary, context_instance=RequestContext(request))

@login_required()
def getInteractionGroups(request, theStudyID):
    siteDictionary = getDictionary(request)
    if request.method == 'POST':
        form_export_type = ExportTypeForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        if form_export_type.is_valid():
            single_interaction_group_pk = form_export_type.cleaned_data['single_export']
            interactionGroup = get_object_or_404(Study, pk=single_interaction_group_pk)
            print interactionGroup
    else:
        theStudy = get_object_or_404(Study, pk=theStudyID)
        interactionGroups = AnimalInteractionGroup.objects.all()
        studyInteractionGroups = []
        for group in interactionGroups:
            if theStudy == group.study:
                studyInteractionGroups.append(group)
        siteDictionary['studyInteractionGroups'] = studyInteractionGroups
        siteDictionary['study'] = theStudy

    return render_to_response('export_interaction_groups.html', siteDictionary, context_instance=RequestContext(request))

@login_required()
def getGroupInteractions(request, theGroupID):
    siteDictionary = getDictionary(request)
    if request.method == 'POST':
        form_export_type = ExportTypeForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        if form_export_type.is_valid():
            is_multi = form_export_type.cleaned_data['is_multi']
            single_interaction_pk = form_export_type.cleaned_data['single_export']
            if is_multi:
                print is_multi
            else:
                interactionGroup = get_object_or_404(Study, pk=single_interaction_pk)
                print interactionGroup
    else:
        theGroup = get_object_or_404(AnimalInteractionGroup, pk=theGroupID)
        interactions = AnimalInteraction.objects.all()
        groupInteractions = []
        for i in interactions:
            if theGroup == i.interaction_group:
                groupInteractions.append(i)
        siteDictionary['groupInteractions'] = groupInteractions
        siteDictionary['group'] = theGroup
        form_export_type = ExportTypeForm()
        siteDictionary['form_export_type'] = form_export_type
    return render_to_response('export_interaction_groupInteractions.html', siteDictionary, context_instance=RequestContext(request))