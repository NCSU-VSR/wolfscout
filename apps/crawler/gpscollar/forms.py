__author__ = 'chris'

from django import forms

class collarDataFileForm(forms.Form):
    file = forms.FileField()

class collarDataFilterForm(forms.Form):
    startDate = forms.DateTimeField(required=False)
    endDate = forms.DateTimeField(required=False)
