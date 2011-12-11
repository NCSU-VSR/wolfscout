__author__ = 'sagentry'
__author__ = 'chris'

### Django Imports ###
from django import forms
### Local Imports
from apps.crawler.cronos.models import *
from apps.wildlife.models import *
from settings.common import CLIMATE_DICTIONARY

class ExportAnimalFilterForm(forms.Form):
    """
    Exporting specific animal demographic informaiton
    """
    def __init__(self, *args, **kwargs):
        super(ExportAnimalFilterForm, self).__init__(*args, **kwargs)
        for field in Animal._meta.fields:
            field_name = str(field.name)
            self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small enableExport_animalFilter'}), label=field_name, initial=True)

class AnimalByNameForm(forms.Form):
    """
    Form for selecting an animal to be filtered by
    """
    def __init__(self, *args, **kwargs):
            super(AnimalByNameForm, self).__init__(*args, **kwargs)
            animals = Animal.objects.all()
            for field in animals:
                field_name = str(field.common_name)
                self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small animalCheckbox'}), initial=False)

class SpeciesByNameForm(forms.Form):
    """
    Form for selecting an animal to be filtered by
    """
    def __init__(self, *args, **kwargs):
            super(SpeciesByNameForm, self).__init__(*args, **kwargs)
            species = Species.objects.all()
            for field in species:
                field_name = str(field.name)
                self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small speciesCheckbox'}), initial=False)

class SexForm(forms.Form):
    """
    Form for selecting an sex to filter by
    """
    def __init__(self, *args, **kwargs):
            super(SexForm, self).__init__(*args, **kwargs)
            self.fields['Male'] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small sexCheckbox'}), label='Male', initial=False)
            self.fields['Female'] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small sexCheckbox'}), label='Female', initial=False)

class AgeForm(forms.Form):
    """
    Form for selecting an age to filter by
    """
    def __init__(self, *args, **kwargs):
        super(AgeForm, self).__init__(*args, **kwargs)
        for field in Animal.AGE_CHOICES:
            field_name = str(field[0])
            self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small ageCheckbox'}), label=field[1], initial=False)

class ExportAnimalTypeForm(forms.Form):
    """
    Form for the type of export to be executed (either CSV of SHAPE)
    """
    is_csv = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small'}))
    is_shape = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small'}))

class ExportCollarDataFilterForm(forms.Form):
    """
    Collar filter form
    """
    def __init__(self, *args, **kwargs):
        super(ExportCollarDataFilterForm, self).__init__(*args, **kwargs)
        for field in CollarData._meta.fields:
            field_name = str(field.name)
            self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small enableExport_collarFilter_ANIMAL_EXPORT_PAGE'}), label=field_name, initial=True)

class ExportWeatherDataFilterForm(forms.Form):
    """
    Weather filter form
    """
    def __init__(self, *args, **kwargs):
        super(ExportWeatherDataFilterForm, self).__init__(*args, **kwargs)
        for field in WeatherDataPoint._meta.fields:
            field_name = str(field.name)
            self.fields[field_name] = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox-small enableExport_weatherFilter_ANIMAL_EXPORT_PAGE'}), label=CLIMATE_DICTIONARY[str(field.name)][0], initial=True)