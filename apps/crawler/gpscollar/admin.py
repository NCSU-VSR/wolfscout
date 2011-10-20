##### Global Imports #####
from django.contrib import admin

from apps.crawler.gpscollar.models import Collar, CollarData

##### Admin Classes ######
class CollarAdmin(admin.ModelAdmin):
    list_display = ('collarID',)
    search_fields = ('collarID',)

class CollarDataAdmin(admin.ModelAdmin):
    list_display = ('collar','LMT_DATETIME','LATITUDE','LONGITUDE','HEIGHT',)
    search_fields = ('collar','LMT_DATETIME','LATITUDE','LONGITUDE','HEIGHT',)

##### Admin Registers ######
admin.site.register(Collar, CollarAdmin)
admin.site.register(CollarData, CollarDataAdmin)