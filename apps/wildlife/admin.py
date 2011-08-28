"""
admin.py is responsible for bridging the gap between your models.py file
and the django admin interface. Update this to update your view of your models.
"""

##### Global Imports #####
from django.contrib import admin

##### Local Imports #####
from wildlife.models import collar, collar_data, species, specimen

##### Admin Classes ######
class collar_admin(admin.ModelAdmin):
    list_display = ('collar_ID',)
    search_fields = ('collar_ID',)

class collar_data_admin(admin.ModelAdmin):
    list_display = ('collar_ID','LMT_DATETIME','LATITUDE','LONGITUDE','HEIGHT',)
    search_fields = ('collar_ID','LMT_DATETIME','LATITUDE','LONGITUDE','HEIGHT',)

class species_admin(admin.ModelAdmin):
    list_display = ('name','notes',)
    search_fields = ('name',)

class specimen_admin(admin.ModelAdmin):
    list_display = ('collar_ID','common_name','species',)
    search_fields = ('collar_ID','common_name','species',)


##### Admin Registers ######
admin.site.register(collar, collar_admin)
admin.site.register(collar_data, collar_data_admin)
admin.site.register(species, species_admin)
admin.site.register(specimen, specimen_admin)