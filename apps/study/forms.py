__author__ = 'scott'

from django.forms.util import ErrorList
from django.utils.safestring import mark_safe

from django import forms
from apps.study.models import Study

"""
class CheckboxSelectMultipleP(forms.CheckboxSelectMultiple):
    def render(self, *args, **kwargs): 
        output = super(CheckboxSelectMultipleP, self).render(*args,**kwargs) 
        return mark_safe(output.replace(u'<ul>', u'').replace(u'</ul>', u'').replace(u'<li>', u'').replace(u'</li>', u''))
        
class StudyForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
                super(StudyForm, self).__init__(*args, **kwargs)
                self.fields['members'].widget = CheckboxSelectMultipleP(choices=self.fields['members'].choices)
                #self.fields['collars'].widget = CheckboxSelectMultipleP(choices=self.fields['collars'].choices)
        class Meta:
            model = Study
"""

class InteractionToBeExportedForm(forms.Form):
    """
    Hidden form field that stores the clicked interaction group export button's pk for reference in the DB
    """
    interaction_to_be_exported = forms.CharField(required=False)

