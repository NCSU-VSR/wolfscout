##### Global Imports #####
from django.contrib.gis import admin

##### Local Imports #####
from apps.study.models import *

##### Admin Classes ######
class StudyAdmin(admin.ModelAdmin):
    list_display = ('title','description','owner',)
    search_fields = ('title','owner',)

class AnimalInteractionAdmin(admin.GeoModelAdmin):
    list_display = ('source_animal_data_point', 'destination_animal_data_point', 'distance')
    search_fields = ('source_animal_data_point', 'destination_animal_data_point', 'distance')

##### Admin Registers ######
admin.site.register(Study, StudyAdmin)
admin.site.register(AnimalInteraction, AnimalInteractionAdmin)