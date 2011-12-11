##### Global Imports #####
from django.contrib.gis import admin

##### Local Imports #####
from apps.study.models import *

##### Admin Classes ######
class ShapeToAnalyzeAdmin(admin.GeoModelAdmin):
    list_display = ('pk',)
    search_fields = ('pk',)

class StudyAdmin(admin.GeoModelAdmin):
    list_display = ('title','description','owner',)
    search_fields = ('title','owner',)

class AnimalInteractionAdmin(admin.GeoModelAdmin):
    list_display = ('source_animal_data_point', 'destination_animal_data_point', 'distance')
    search_fields = ('source_animal_data_point', 'destination_animal_data_point', 'distance')

class AnimalInteractionGroupAdmin(admin.GeoModelAdmin):
    list_display = ('study','distance')
    search_fields = ('study','distance')

##### Admin Registers ######
admin.site.register(ShapeToAnalyze, ShapeToAnalyzeAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(AnimalInteraction, AnimalInteractionAdmin)
admin.site.register(AnimalInteractionGroup, AnimalInteractionGroupAdmin)

