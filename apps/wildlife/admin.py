"""
admin.py is responsible for bridging the gap between your models.py file
and the django admin interface. Update this to update your view of your models.
"""

##### Global Imports #####
from django.contrib import admin

##### Local Imports #####
from wildlife.models import Collar, CollarData, Species, Specimen

##### Admin Classes ######
class CollarAdmin(admin.ModelAdmin):
    list_display = ('collarID',)
    search_fields = ('collarID',)

class CollarDataAdmin(admin.ModelAdmin):
    list_display = ('collar','LMT_DATETIME','LATITUDE','LONGITUDE','HEIGHT',)
    search_fields = ('collar','LMT_DATETIME','LATITUDE','LONGITUDE','HEIGHT',)

class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('name','notes',)
    search_fields = ('name',)

class SpecimenAdmin(admin.ModelAdmin):
    list_display = ('collar','common_name','species',)
    search_fields = ('collar','common_name','species',)


##### Admin Registers ######
admin.site.register(Collar, CollarAdmin)
admin.site.register(CollarData, CollarDataAdmin)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Specimen, SpecimenAdmin)