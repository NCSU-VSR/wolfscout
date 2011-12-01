"""
admin.py is responsible for bridging the gap between your models.py file
and the django admin interface. Update this to update your view of your models.
"""

##### Global Imports #####
from django.contrib.gis import admin

##### Local Imports #####
from apps.wildlife.models import Species, Specimen

##### Admin Classes ######
class SpeciesAdmin(admin.GeoModelAdmin):
    list_display = ('name','notes',)
    search_fields = ('name',)

class SpecimenAdmin(admin.GeoModelAdmin):
    list_display = ('collar','common_name','species',)
    search_fields = ('collar','common_name','species',)

##### Admin Registers ######
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Specimen, SpecimenAdmin)