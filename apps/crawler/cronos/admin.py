__author__ = 'chris'
 ##### Global Imports #####
from django.contrib import admin

from apps.crawler.cronos.models import Station, WeatherDataPoint

##### Admin Classes ######
class StationAdmin(admin.ModelAdmin):
    list_display = ('station_code','LOCATION','name',)
    search_fields = ('station_code','LOCATION','name',)

class WeatherDataPointAdmin(admin.ModelAdmin):
    list_display = ('id','temp','station',)
    search_fields = ('id','temp','station',)

##### Admin Registers ######
admin.site.register(Station, StationAdmin)
admin.site.register(WeatherDataPoint, WeatherDataPointAdmin)
