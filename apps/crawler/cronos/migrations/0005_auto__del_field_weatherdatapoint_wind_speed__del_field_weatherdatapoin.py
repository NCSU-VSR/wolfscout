# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'WeatherDataPoint.wind_speed'
        db.delete_column('cronos_weatherdatapoint', 'wind_speed')

        # Deleting field 'WeatherDataPoint.solar_radiation'
        db.delete_column('cronos_weatherdatapoint', 'solar_radiation')

        # Deleting field 'WeatherDataPoint.soil_temperature'
        db.delete_column('cronos_weatherdatapoint', 'soil_temperature')

        # Deleting field 'WeatherDataPoint.wind_speed2'
        db.delete_column('cronos_weatherdatapoint', 'wind_speed2')

        # Deleting field 'WeatherDataPoint.cloud_cover'
        db.delete_column('cronos_weatherdatapoint', 'cloud_cover')

        # Deleting field 'WeatherDataPoint.precipitation'
        db.delete_column('cronos_weatherdatapoint', 'precipitation')

        # Deleting field 'WeatherDataPoint.wind_direction'
        db.delete_column('cronos_weatherdatapoint', 'wind_direction')

        # Deleting field 'WeatherDataPoint.soil_moisture'
        db.delete_column('cronos_weatherdatapoint', 'soil_moisture')

        # Deleting field 'WeatherDataPoint.temperature10'
        db.delete_column('cronos_weatherdatapoint', 'temperature10')

        # Deleting field 'WeatherDataPoint.visibility'
        db.delete_column('cronos_weatherdatapoint', 'visibility')

        # Deleting field 'WeatherDataPoint.humidity'
        db.delete_column('cronos_weatherdatapoint', 'humidity')

        # Deleting field 'WeatherDataPoint.wind_gust'
        db.delete_column('cronos_weatherdatapoint', 'wind_gust')

        # Deleting field 'WeatherDataPoint.humidity10'
        db.delete_column('cronos_weatherdatapoint', 'humidity10')

        # Deleting field 'WeatherDataPoint.barometric_pressure'
        db.delete_column('cronos_weatherdatapoint', 'barometric_pressure')

        # Deleting field 'WeatherDataPoint.distance_from_collar'
        db.delete_column('cronos_weatherdatapoint', 'distance_from_collar')

        # Deleting field 'WeatherDataPoint.photosynthetically_active_radiation'
        db.delete_column('cronos_weatherdatapoint', 'photosynthetically_active_radiation')

        # Deleting field 'WeatherDataPoint.leaf_wetness'
        db.delete_column('cronos_weatherdatapoint', 'leaf_wetness')

        # Deleting field 'WeatherDataPoint.temperature'
        db.delete_column('cronos_weatherdatapoint', 'temperature')

        # Adding field 'WeatherDataPoint.altimeter'
        db.add_column('cronos_weatherdatapoint', 'altimeter', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.dew'
        db.add_column('cronos_weatherdatapoint', 'dew', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.groundsnow'
        db.add_column('cronos_weatherdatapoint', 'groundsnow', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.gust'
        db.add_column('cronos_weatherdatapoint', 'gust', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.gustavg'
        db.add_column('cronos_weatherdatapoint', 'gustavg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.lev1'
        db.add_column('cronos_weatherdatapoint', 'lev1', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.lev2'
        db.add_column('cronos_weatherdatapoint', 'lev2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.lev3'
        db.add_column('cronos_weatherdatapoint', 'lev3', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.obscur'
        db.add_column('cronos_weatherdatapoint', 'obscur', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.par'
        db.add_column('cronos_weatherdatapoint', 'par', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.paravg'
        db.add_column('cronos_weatherdatapoint', 'paravg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.parmax'
        db.add_column('cronos_weatherdatapoint', 'parmax', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.parmin'
        db.add_column('cronos_weatherdatapoint', 'parmin', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.pind'
        db.add_column('cronos_weatherdatapoint', 'pind', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.precip'
        db.add_column('cronos_weatherdatapoint', 'precip', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.precip24'
        db.add_column('cronos_weatherdatapoint', 'precip24', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.precip6'
        db.add_column('cronos_weatherdatapoint', 'precip6', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.pres'
        db.add_column('cronos_weatherdatapoint', 'pres', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.presavg'
        db.add_column('cronos_weatherdatapoint', 'presavg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.presch'
        db.add_column('cronos_weatherdatapoint', 'presch', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.presmax'
        db.add_column('cronos_weatherdatapoint', 'presmax', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.presmin'
        db.add_column('cronos_weatherdatapoint', 'presmin', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.remarks'
        db.add_column('cronos_weatherdatapoint', 'remarks', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.rh'
        db.add_column('cronos_weatherdatapoint', 'rh', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.rh10'
        db.add_column('cronos_weatherdatapoint', 'rh10', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.rh10avg'
        db.add_column('cronos_weatherdatapoint', 'rh10avg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.rh10max'
        db.add_column('cronos_weatherdatapoint', 'rh10max', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.rh10min'
        db.add_column('cronos_weatherdatapoint', 'rh10min', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.rhavg'
        db.add_column('cronos_weatherdatapoint', 'rhavg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.rhmax'
        db.add_column('cronos_weatherdatapoint', 'rhmax', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.rhmin'
        db.add_column('cronos_weatherdatapoint', 'rhmin', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.slp'
        db.add_column('cronos_weatherdatapoint', 'slp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.sm'
        db.add_column('cronos_weatherdatapoint', 'sm', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.smavg'
        db.add_column('cronos_weatherdatapoint', 'smavg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.smmax'
        db.add_column('cronos_weatherdatapoint', 'smmax', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.smmin'
        db.add_column('cronos_weatherdatapoint', 'smmin', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.sr'
        db.add_column('cronos_weatherdatapoint', 'sr', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.sravg'
        db.add_column('cronos_weatherdatapoint', 'sravg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.srmax'
        db.add_column('cronos_weatherdatapoint', 'srmax', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.srmin'
        db.add_column('cronos_weatherdatapoint', 'srmin', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.st'
        db.add_column('cronos_weatherdatapoint', 'st', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.stavg'
        db.add_column('cronos_weatherdatapoint', 'stavg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.stmax'
        db.add_column('cronos_weatherdatapoint', 'stmax', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.stmin'
        db.add_column('cronos_weatherdatapoint', 'stmin', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.temp'
        db.add_column('cronos_weatherdatapoint', 'temp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.temp10'
        db.add_column('cronos_weatherdatapoint', 'temp10', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.temp10avg'
        db.add_column('cronos_weatherdatapoint', 'temp10avg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.temp10max'
        db.add_column('cronos_weatherdatapoint', 'temp10max', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.temp10min'
        db.add_column('cronos_weatherdatapoint', 'temp10min', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.tempavg'
        db.add_column('cronos_weatherdatapoint', 'tempavg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.tempmax'
        db.add_column('cronos_weatherdatapoint', 'tempmax', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.tempmax24'
        db.add_column('cronos_weatherdatapoint', 'tempmax24', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.tempmax6'
        db.add_column('cronos_weatherdatapoint', 'tempmax6', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.tempmin'
        db.add_column('cronos_weatherdatapoint', 'tempmin', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.tempmin24'
        db.add_column('cronos_weatherdatapoint', 'tempmin24', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.tempmin6'
        db.add_column('cronos_weatherdatapoint', 'tempmin6', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.vis'
        db.add_column('cronos_weatherdatapoint', 'vis', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.wd'
        db.add_column('cronos_weatherdatapoint', 'wd', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.wd02'
        db.add_column('cronos_weatherdatapoint', 'wd02', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.wd02avg'
        db.add_column('cronos_weatherdatapoint', 'wd02avg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.wdavg'
        db.add_column('cronos_weatherdatapoint', 'wdavg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.weather'
        db.add_column('cronos_weatherdatapoint', 'weather', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.ws'
        db.add_column('cronos_weatherdatapoint', 'ws', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.ws02'
        db.add_column('cronos_weatherdatapoint', 'ws02', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.ws02avg'
        db.add_column('cronos_weatherdatapoint', 'ws02avg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.wsavg'
        db.add_column('cronos_weatherdatapoint', 'wsavg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'WeatherDataPoint.wind_speed'
        db.add_column('cronos_weatherdatapoint', 'wind_speed', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.solar_radiation'
        db.add_column('cronos_weatherdatapoint', 'solar_radiation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.soil_temperature'
        db.add_column('cronos_weatherdatapoint', 'soil_temperature', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.wind_speed2'
        db.add_column('cronos_weatherdatapoint', 'wind_speed2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.cloud_cover'
        db.add_column('cronos_weatherdatapoint', 'cloud_cover', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.precipitation'
        db.add_column('cronos_weatherdatapoint', 'precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.wind_direction'
        db.add_column('cronos_weatherdatapoint', 'wind_direction', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.soil_moisture'
        db.add_column('cronos_weatherdatapoint', 'soil_moisture', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.temperature10'
        db.add_column('cronos_weatherdatapoint', 'temperature10', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.visibility'
        db.add_column('cronos_weatherdatapoint', 'visibility', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.humidity'
        db.add_column('cronos_weatherdatapoint', 'humidity', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.wind_gust'
        db.add_column('cronos_weatherdatapoint', 'wind_gust', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.humidity10'
        db.add_column('cronos_weatherdatapoint', 'humidity10', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.barometric_pressure'
        db.add_column('cronos_weatherdatapoint', 'barometric_pressure', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.distance_from_collar'
        db.add_column('cronos_weatherdatapoint', 'distance_from_collar', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.photosynthetically_active_radiation'
        db.add_column('cronos_weatherdatapoint', 'photosynthetically_active_radiation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.leaf_wetness'
        db.add_column('cronos_weatherdatapoint', 'leaf_wetness', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.temperature'
        db.add_column('cronos_weatherdatapoint', 'temperature', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Deleting field 'WeatherDataPoint.altimeter'
        db.delete_column('cronos_weatherdatapoint', 'altimeter')

        # Deleting field 'WeatherDataPoint.dew'
        db.delete_column('cronos_weatherdatapoint', 'dew')

        # Deleting field 'WeatherDataPoint.groundsnow'
        db.delete_column('cronos_weatherdatapoint', 'groundsnow')

        # Deleting field 'WeatherDataPoint.gust'
        db.delete_column('cronos_weatherdatapoint', 'gust')

        # Deleting field 'WeatherDataPoint.gustavg'
        db.delete_column('cronos_weatherdatapoint', 'gustavg')

        # Deleting field 'WeatherDataPoint.lev1'
        db.delete_column('cronos_weatherdatapoint', 'lev1')

        # Deleting field 'WeatherDataPoint.lev2'
        db.delete_column('cronos_weatherdatapoint', 'lev2')

        # Deleting field 'WeatherDataPoint.lev3'
        db.delete_column('cronos_weatherdatapoint', 'lev3')

        # Deleting field 'WeatherDataPoint.obscur'
        db.delete_column('cronos_weatherdatapoint', 'obscur')

        # Deleting field 'WeatherDataPoint.par'
        db.delete_column('cronos_weatherdatapoint', 'par')

        # Deleting field 'WeatherDataPoint.paravg'
        db.delete_column('cronos_weatherdatapoint', 'paravg')

        # Deleting field 'WeatherDataPoint.parmax'
        db.delete_column('cronos_weatherdatapoint', 'parmax')

        # Deleting field 'WeatherDataPoint.parmin'
        db.delete_column('cronos_weatherdatapoint', 'parmin')

        # Deleting field 'WeatherDataPoint.pind'
        db.delete_column('cronos_weatherdatapoint', 'pind')

        # Deleting field 'WeatherDataPoint.precip'
        db.delete_column('cronos_weatherdatapoint', 'precip')

        # Deleting field 'WeatherDataPoint.precip24'
        db.delete_column('cronos_weatherdatapoint', 'precip24')

        # Deleting field 'WeatherDataPoint.precip6'
        db.delete_column('cronos_weatherdatapoint', 'precip6')

        # Deleting field 'WeatherDataPoint.pres'
        db.delete_column('cronos_weatherdatapoint', 'pres')

        # Deleting field 'WeatherDataPoint.presavg'
        db.delete_column('cronos_weatherdatapoint', 'presavg')

        # Deleting field 'WeatherDataPoint.presch'
        db.delete_column('cronos_weatherdatapoint', 'presch')

        # Deleting field 'WeatherDataPoint.presmax'
        db.delete_column('cronos_weatherdatapoint', 'presmax')

        # Deleting field 'WeatherDataPoint.presmin'
        db.delete_column('cronos_weatherdatapoint', 'presmin')

        # Deleting field 'WeatherDataPoint.remarks'
        db.delete_column('cronos_weatherdatapoint', 'remarks')

        # Deleting field 'WeatherDataPoint.rh'
        db.delete_column('cronos_weatherdatapoint', 'rh')

        # Deleting field 'WeatherDataPoint.rh10'
        db.delete_column('cronos_weatherdatapoint', 'rh10')

        # Deleting field 'WeatherDataPoint.rh10avg'
        db.delete_column('cronos_weatherdatapoint', 'rh10avg')

        # Deleting field 'WeatherDataPoint.rh10max'
        db.delete_column('cronos_weatherdatapoint', 'rh10max')

        # Deleting field 'WeatherDataPoint.rh10min'
        db.delete_column('cronos_weatherdatapoint', 'rh10min')

        # Deleting field 'WeatherDataPoint.rhavg'
        db.delete_column('cronos_weatherdatapoint', 'rhavg')

        # Deleting field 'WeatherDataPoint.rhmax'
        db.delete_column('cronos_weatherdatapoint', 'rhmax')

        # Deleting field 'WeatherDataPoint.rhmin'
        db.delete_column('cronos_weatherdatapoint', 'rhmin')

        # Deleting field 'WeatherDataPoint.slp'
        db.delete_column('cronos_weatherdatapoint', 'slp')

        # Deleting field 'WeatherDataPoint.sm'
        db.delete_column('cronos_weatherdatapoint', 'sm')

        # Deleting field 'WeatherDataPoint.smavg'
        db.delete_column('cronos_weatherdatapoint', 'smavg')

        # Deleting field 'WeatherDataPoint.smmax'
        db.delete_column('cronos_weatherdatapoint', 'smmax')

        # Deleting field 'WeatherDataPoint.smmin'
        db.delete_column('cronos_weatherdatapoint', 'smmin')

        # Deleting field 'WeatherDataPoint.sr'
        db.delete_column('cronos_weatherdatapoint', 'sr')

        # Deleting field 'WeatherDataPoint.sravg'
        db.delete_column('cronos_weatherdatapoint', 'sravg')

        # Deleting field 'WeatherDataPoint.srmax'
        db.delete_column('cronos_weatherdatapoint', 'srmax')

        # Deleting field 'WeatherDataPoint.srmin'
        db.delete_column('cronos_weatherdatapoint', 'srmin')

        # Deleting field 'WeatherDataPoint.st'
        db.delete_column('cronos_weatherdatapoint', 'st')

        # Deleting field 'WeatherDataPoint.stavg'
        db.delete_column('cronos_weatherdatapoint', 'stavg')

        # Deleting field 'WeatherDataPoint.stmax'
        db.delete_column('cronos_weatherdatapoint', 'stmax')

        # Deleting field 'WeatherDataPoint.stmin'
        db.delete_column('cronos_weatherdatapoint', 'stmin')

        # Deleting field 'WeatherDataPoint.temp'
        db.delete_column('cronos_weatherdatapoint', 'temp')

        # Deleting field 'WeatherDataPoint.temp10'
        db.delete_column('cronos_weatherdatapoint', 'temp10')

        # Deleting field 'WeatherDataPoint.temp10avg'
        db.delete_column('cronos_weatherdatapoint', 'temp10avg')

        # Deleting field 'WeatherDataPoint.temp10max'
        db.delete_column('cronos_weatherdatapoint', 'temp10max')

        # Deleting field 'WeatherDataPoint.temp10min'
        db.delete_column('cronos_weatherdatapoint', 'temp10min')

        # Deleting field 'WeatherDataPoint.tempavg'
        db.delete_column('cronos_weatherdatapoint', 'tempavg')

        # Deleting field 'WeatherDataPoint.tempmax'
        db.delete_column('cronos_weatherdatapoint', 'tempmax')

        # Deleting field 'WeatherDataPoint.tempmax24'
        db.delete_column('cronos_weatherdatapoint', 'tempmax24')

        # Deleting field 'WeatherDataPoint.tempmax6'
        db.delete_column('cronos_weatherdatapoint', 'tempmax6')

        # Deleting field 'WeatherDataPoint.tempmin'
        db.delete_column('cronos_weatherdatapoint', 'tempmin')

        # Deleting field 'WeatherDataPoint.tempmin24'
        db.delete_column('cronos_weatherdatapoint', 'tempmin24')

        # Deleting field 'WeatherDataPoint.tempmin6'
        db.delete_column('cronos_weatherdatapoint', 'tempmin6')

        # Deleting field 'WeatherDataPoint.vis'
        db.delete_column('cronos_weatherdatapoint', 'vis')

        # Deleting field 'WeatherDataPoint.wd'
        db.delete_column('cronos_weatherdatapoint', 'wd')

        # Deleting field 'WeatherDataPoint.wd02'
        db.delete_column('cronos_weatherdatapoint', 'wd02')

        # Deleting field 'WeatherDataPoint.wd02avg'
        db.delete_column('cronos_weatherdatapoint', 'wd02avg')

        # Deleting field 'WeatherDataPoint.wdavg'
        db.delete_column('cronos_weatherdatapoint', 'wdavg')

        # Deleting field 'WeatherDataPoint.weather'
        db.delete_column('cronos_weatherdatapoint', 'weather')

        # Deleting field 'WeatherDataPoint.ws'
        db.delete_column('cronos_weatherdatapoint', 'ws')

        # Deleting field 'WeatherDataPoint.ws02'
        db.delete_column('cronos_weatherdatapoint', 'ws02')

        # Deleting field 'WeatherDataPoint.ws02avg'
        db.delete_column('cronos_weatherdatapoint', 'ws02avg')

        # Deleting field 'WeatherDataPoint.wsavg'
        db.delete_column('cronos_weatherdatapoint', 'wsavg')


    models = {
        'cronos.station': {
            'LOCATION': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'Meta': {'object_name': 'Station'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'climatediv': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'elevation': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'huc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'network': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'station_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'})
        },
        'cronos.weatherdatapoint': {
            'Meta': {'object_name': 'WeatherDataPoint'},
            'altimeter': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'dew': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'groundsnow': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'gust': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'gustavg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lev1': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'lev2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'lev3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'obscur': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'par': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'paravg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'parmax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'parmin': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'pind': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'precip': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'precip24': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'precip6': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'pres': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'presavg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'presch': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'presmax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'presmin': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rh': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'rh10': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'rh10avg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'rh10max': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'rh10min': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'rhavg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'rhmax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'rhmin': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'slp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'sm': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'smavg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'smmax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'smmin': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'sr': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'sravg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'srmax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'srmin': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'st': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cronos.Station']", 'null': 'True', 'blank': 'True'}),
            'stavg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'stmax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'stmin': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'temp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'temp10': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'temp10avg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'temp10max': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'temp10min': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'tempavg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'tempmax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'tempmax24': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'tempmax6': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'tempmin': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'tempmin24': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'tempmin6': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'vis': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'wd': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'wd02': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'wd02avg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'wdavg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'weather': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'ws': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'ws02': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'ws02avg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'wsavg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'})
        }
    }

    complete_apps = ['cronos']
