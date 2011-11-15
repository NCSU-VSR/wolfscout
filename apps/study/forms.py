__author__ = 'scott'

from django.forms.util import ErrorList
from django.forms import ModelForm, ValidationError
from django.utils.safestring import mark_safe

from django import forms
from apps.study.models import Study
from apps.crawler.gpscollar.models import Collar

class CheckboxSelectMultipleP(forms.CheckboxSelectMultiple):
    def render(self, *args, **kwargs): 
        output = super(CheckboxSelectMultipleP, self).render(*args,**kwargs) 
        return mark_safe(output.replace(u'<ul>', u'').replace(u'</ul>', u'').replace(u'<li>', u'').replace(u'</li>', u''))

class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return u''
        return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="messages red"><span></span>%s</div>' % e for e in self])
        
class StudyForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
                super(StudyForm, self).__init__(*args, **kwargs)
                self.fields['members'].widget = CheckboxSelectMultipleP(choices=self.fields['members'].choices)
                #self.fields['collars'].widget = CheckboxSelectMultipleP(choices=self.fields['collars'].choices)
        class Meta:
            model = Study
            

