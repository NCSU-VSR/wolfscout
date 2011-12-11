__author__ = 'sagentry'

__author__ = 'chris'

### Django Imports ###
from django.forms.util import ErrorList

class DivErrorList(ErrorList):
    """
    Commonly used formatted error list when a form validation returns false.  Follows the formatting of our
    wolfscout templates
    """
    def __unicode__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return u''
        return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="messages red"><span></span>%s</div>' % e for e in self])