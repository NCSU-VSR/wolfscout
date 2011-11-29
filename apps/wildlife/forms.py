__author__ = 'sagentry'

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

class ExportSpecimenFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ExportSpecimenFilterForm, self).__init__(*args, **kwargs)
        for field in Specimen._meta.fields:
            field_name = str(field.name)
            self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small enableExport_specimenFilter'}), label=field_name, initial=True)