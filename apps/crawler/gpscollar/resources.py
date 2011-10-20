from djangorestframework.resources import ModelResource
from models import Collar, CollarData

class CollarResource(ModelResource):
    model = Collar
    fields = ('collarID','url',)
    ordering = ('collarID',)

class CollarDataResource(ModelResource):
    model = CollarData
    fields = ('collar', 'GMT_DATETIME', 'LMT_DATETIME', 'LOCATION',
              'NAV','DATE_ADDED','url')
    ordering = ('id',)