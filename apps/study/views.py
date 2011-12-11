### Django Imports ####
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
### Global Imports ####
### Local Imports ####
from apps.general.views import getDictionary
from apps.study.models import *
from apps.study.forms import *
from apps.general.forms import *
### Views ####

"""
@login_required()
def studies(request):
    siteDictionary = getDictionary(request)
    return render_to_response('studies.html', siteDictionary, context_instance=RequestContext(request))
  
@login_required()  
def study(request, theStudyID):
    study = get_object_or_404(Study, pk=theStudyID)
    siteDictionary = getDictionary(request)
    siteDictionary['study'] = study
    return render_to_response('study.html', siteDictionary, context_instance=RequestContext(request))
        
@login_required()  
def edit(request, theStudyID):
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
"""

@login_required()
def interactions(request):
    """
    View for export_interactions
    """
    siteDictionary = getDictionary(request)
    siteDictionary['studies'] = Study.objects.all()
    return render_to_response('export_interactions.html', siteDictionary, context_instance=RequestContext(request))

@login_required()
def getInteractionGroups(request, theStudyID):
    """
    Shows the interaction groups and allows for exportation of that interaction group shape files via zip file
    """
    siteDictionary = getDictionary(request)
    if request.method == 'POST':
        form_interaction_to_be_exported = InteractionToBeExportedForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        if form_interaction_to_be_exported.is_valid():
            interaction_group_pk = form_interaction_to_be_exported.cleaned_data['interaction_to_be_exported']
            interactionGroup = get_object_or_404(AnimalInteractionGroup, pk=interaction_group_pk)
            return HttpResponseRedirect('/media/' + str(interactionGroup.zip_file))
    else:
        theStudy = get_object_or_404(Study, pk=theStudyID)
        interactionGroups = AnimalInteractionGroup.objects.all()
        studyInteractionGroups = []
        for group in interactionGroups:
            if theStudy == group.study:
                studyInteractionGroups.append(group)
        siteDictionary['studyInteractionGroups'] = studyInteractionGroups
        siteDictionary['study'] = theStudy

        form_interaction_to_be_exported = InteractionToBeExportedForm()
        siteDictionary['form_interaction_to_be_exported'] = form_interaction_to_be_exported
    return render_to_response('export_interaction_groups.html', siteDictionary, context_instance=RequestContext(request))

@login_required()
def getGroupInteractions(request, theGroupID):
    """
    Shows the interaction groups specific interactions in view
    """
    siteDictionary = getDictionary(request)
    theGroup = get_object_or_404(AnimalInteractionGroup, pk=theGroupID)
    interactions = AnimalInteraction.objects.all()
    groupInteractions = []
    for i in interactions:
        if theGroup == i.interaction_group:
            groupInteractions.append(i)
    siteDictionary['groupInteractions'] = groupInteractions
    siteDictionary['group'] = theGroup
    return render_to_response('export_interaction_groupInteractions.html', siteDictionary, context_instance=RequestContext(request))