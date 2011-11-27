##### Global Imports #####
from django.contrib.gis import admin

##### Local Imports #####
from apps.study.models import Study

##### Admin Classes ######
class StudyAdmin(admin.ModelAdmin):
    list_display = ('title','description','owner',)
    search_fields = ('title','owner',)


##### Admin Registers ######
admin.site.register(Study, StudyAdmin)