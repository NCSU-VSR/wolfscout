__author__ = 'chris'

### Django Imports ###
from django.forms.util import ErrorList
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django import forms
### Local Imports
from apps.crawler.gpscollar.collar import *
from apps.crawler.gpscollar.support import *
from apps.crawler.cronos.models import *
from apps.wildlife.models import *

class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return u''
        return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="messages red"><span></span>%s</div>' % e for e in self])
        
class collarDataFileForm(forms.Form):
    file = forms.FileField()

class collarDataFilterForm(forms.Form):
    startDate = forms.DateTimeField(required=False)
    endDate = forms.DateTimeField(required=False)

class CollarIDForm(forms.Form):
    collar_id = forms.ModelChoiceField(Collar.objects.all())
    
class InteractionsDistanceForm(forms.Form):
    distance_in_km = forms.RegexField(initial=DISTANCE_TO_SEARCH, required=False, max_length=31, regex=r'^([0-9]*|\d*\.\d{1}?\d*)$', error_message = ("This value must contain only numbers and one decimal point."))
    selected_collars = forms.CharField(required=False, widget=forms.Textarea(attrs={'readonly':'readonly'}))#,widget=forms.HiddenInput)
    
class UploadShapeFileForm(forms.Form):
    shape_file = forms.FileField(required=False)
    selected_shapes = forms.CharField(required=False, widget=forms.Textarea(attrs={'readonly':'readonly'}))#,widget=forms.HiddenInput)
         
class ExportCollarDataForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ExportCollarDataForm, self).__init__(*args, **kwargs)
        collars = Collar.objects.all()
        for collar in collars:
            field_name = str(collar.collarID)
            self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small enableExport'}), label=field_name)

class ExportTypeForm(forms.Form):
    is_multi = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small'}))
    add_weather = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small'}))
    single_collar = forms.CharField(required=False)

class ExportCollarDataFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ExportCollarDataFilterForm, self).__init__(*args, **kwargs)
        for field in CollarData._meta.fields:
            field_name = str(field.name)
            self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small enableExport_collarFilter'}), label=field_name, initial=True)
            
class ExportWeatherDataFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ExportWeatherDataFilterForm, self).__init__(*args, **kwargs)
        for field in WeatherDataPoint._meta.fields:
            field_name = str(field.name)
            self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small enableExport_weatherFilter'}), label=field_name, initial=True)