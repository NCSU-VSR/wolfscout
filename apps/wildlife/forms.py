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

class SpecimenByNameForm(forms.Form):
    def __init__(self, *args, **kwargs):
            super(SpecimenByNameForm, self).__init__(*args, **kwargs)
            specimens = Specimen.objects.all()
            for field in specimens:
                field_name = str(field.pk)
                self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small specimenCheckbox'}), label=field_name, initial=False)

class SpeciesByNameForm(forms.Form):
    def __init__(self, *args, **kwargs):
            super(SpeciesByNameForm, self).__init__(*args, **kwargs)
            species = Species.objects.all()
            for field in species:
                field_name = str(field.pk)
                self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small enableExport_speciesName'}), label=field_name, initial=False)

class SexForm(forms.Form):
    def __init__(self, *args, **kwargs):
                super(SexForm, self).__init__(*args, **kwargs)
                self.fields['Male'] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small'}), label='Male', initial=False)
                self.fields['Female'] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small'}), label='Female', initial=False)