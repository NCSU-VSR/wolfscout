### Django Imports ####
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.sitemaps import ping_google
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm, ValidationError
from django import forms
from django.template import RequestContext

### Global Imports ####
import datetime
### Local Imports ###
from apps.crawler.gpscollar.collar import CollarParser
from apps.crawler.gpscollar.models import Collar
from apps.crawler.gpscollar.models import CollarData
from apps.general.views import getDictionary
from apps.crawler.gpscollar.forms import collarDataFileForm
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
    return render_to_response('collar.html', siteDictionary, context_instance=RequestContext(request))
    
def getCollarData(request, theCollarID):
    """
    """
    theCollar = get_object_or_404(Collar, collarID=theCollarID)
    collarDatas = CollarData.objects.filter(collar=theCollar)
    siteDictionary = getDictionary(request)
    siteDictionary['collar'] = theCollar
    siteDictionary['collarDatas']=collarDatas
    return render_to_response('collarData.html', siteDictionary)
    
from django.forms.util import ErrorList
class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return u''
        return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="messages red"><span></span>%s</div>' % e for e in self])

class CollarIDForm(forms.Form):
    collar_id = forms.ModelChoiceField(Collar.objects.all())

def collarForm(request):
    if request.method == 'POST':
        form = CollarIDForm(request.POST, error_class=DivErrorList, auto_id='id_%s')
        if form.is_valid():
            theID = form.cleaned_data['collar_id']
            return HttpResponseRedirect('/collarData/' + str(theID) + "/")
    else:
        form = CollarIDForm()
    return render_to_response('collar.html', {'form': form,}, context_instance=RequestContext(request))


def uploadCollarDataFile(request):
    if request.method == 'POST':
        form = collarDataFileForm(request.POST, request.FILES)
        if form.is_valid():
            processCollarDataFile(request.FILES['file'])
            return HttpResponseRedirect('/')
    else:
        form = collarDataFileForm()
    return render_to_response('uploadCollarData.html', {'form': form},context_instance=RequestContext(request))

def processCollarDataFile(fileToWrite):
    """
    Start by saving the file to disk based on a timestamp
    Then After write has been completed please process the file
    """
    finalFilename = '/opt/webapps/ncsu/collarFiles/'+fileToWrite.name

    destination = open(finalFilename, 'wb+')
    for chunk in fileToWrite.chunks():
        destination.write(chunk)
    destination.close()

    #time to process the file
    cp = CollarParser(finalFilename)
    cp.processCSVIntoDatabase()

    return 0

