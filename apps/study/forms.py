__author__ = 'scott'

from django import forms
from apps.study.models import Study
from django.forms.util import ErrorList

class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return u''
        return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="messages red"><span></span>%s</div>' % e for e in self])
        
class EditStudyForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField()
    members = forms.ModelChoiceField(Study.objects.filter(pk=1))
