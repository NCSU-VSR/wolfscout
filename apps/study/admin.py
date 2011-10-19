##### Global Imports #####
from django.contrib import admin

##### Local Imports #####
from apps.study.models import Experiment

##### Admin Classes ######
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('owner',)
    search_fields = ('owner',)


##### Admin Registers ######
admin.site.register(Experiment, ExperimentAdmin)