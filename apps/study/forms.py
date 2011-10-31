__author__ = 'scott'

from django.forms.util import ErrorList
from django.forms import ModelForm, ValidationError

from django import forms
from apps.study.models import Study

class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return u''
        return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="messages red"><span></span>%s</div>' % e for e in self])
        
class EditStudyForm(ModelForm):
        class Meta:
            model = Study
