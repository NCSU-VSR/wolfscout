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
from settings.common import CLIMATE_DICTIONARY
        
class collarDataFileForm(forms.Form):
    file = forms.FileField()

class collarDataFilterForm(forms.Form):
    startDate = forms.DateTimeField(required=False)
    endDate = forms.DateTimeField(required=False)

class CollarIDForm(forms.Form):
    collar_id = forms.ModelChoiceField(Collar.objects.all())
    
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
    is_multi_csv = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small'}))
    is_multi_shape = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small'}))
    is_single_csv = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small'}))
    is_single_shape = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small'}))
    single_export = forms.CharField(required=False)

class ExportCollarDataFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ExportCollarDataFilterForm, self).__init__(*args, **kwargs)
        for field in CollarData._meta.fields:
            field_name = str(field.name)
            self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small enableExport_collarFilter_COLLAR_EXPORT_PAGE'}), label=field_name, initial=True)
            
class ExportWeatherDataFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ExportWeatherDataFilterForm, self).__init__(*args, **kwargs)
        for field in WeatherDataPoint._meta.fields:
            field_name = str(field.name)
            self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small enableExport_weatherFilter_COLLAR_EXPORT_PAGE'}), label=CLIMATE_DICTIONARY[str(field.name)][0], initial=True)

