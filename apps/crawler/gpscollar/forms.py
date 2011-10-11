__author__ = 'chris'

from django import forms

class collarDataFileForm(forms.Form):
    file = forms.FileField()