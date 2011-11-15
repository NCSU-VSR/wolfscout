# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'WeatherDataPoint.extreme_events'
        db.delete_column('cronos_weatherdatapoint', 'extreme_events')

        # Deleting field 'WeatherDataPoint.sunset'
        db.delete_column('cronos_weatherdatapoint', 'sunset')

        # Deleting field 'WeatherDataPoint.heat_index'
        db.delete_column('cronos_weatherdatapoint', 'heat_index')

        # Deleting field 'WeatherDataPoint.sunrise'
        db.delete_column('cronos_weatherdatapoint', 'sunrise')

        # Adding field 'WeatherDataPoint.temperature10'
        db.add_column('cronos_weatherdatapoint', 'temperature10', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.humidity10'
        db.add_column('cronos_weatherdatapoint', 'humidity10', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.wind_speed2'
        db.add_column('cronos_weatherdatapoint', 'wind_speed2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.wind_gust'
        db.add_column('cronos_weatherdatapoint', 'wind_gust', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.solar_radiation'
        db.add_column('cronos_weatherdatapoint', 'solar_radiation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.photosynthetically_active_radiation'
        db.add_column('cronos_weatherdatapoint', 'photosynthetically_active_radiation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.soil_temperature'
        db.add_column('cronos_weatherdatapoint', 'soil_temperature', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.soil_moisture'
        db.add_column('cronos_weatherdatapoint', 'soil_moisture', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.leaf_wetness'
        db.add_column('cronos_weatherdatapoint', 'leaf_wetness', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'WeatherDataPoint.extreme_events'
        db.add_column('cronos_weatherdatapoint', 'extreme_events', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.sunset'
        db.add_column('cronos_weatherdatapoint', 'sunset', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 11, 14)), keep_default=False)

        # Adding field 'WeatherDataPoint.heat_index'
        db.add_column('cronos_weatherdatapoint', 'heat_index', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'WeatherDataPoint.sunrise'
        db.add_column('cronos_weatherdatapoint', 'sunrise', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 11, 14)), keep_default=False)

        # Deleting field 'WeatherDataPoint.temperature10'
        db.delete_column('cronos_weatherdatapoint', 'temperature10')

        # Deleting field 'WeatherDataPoint.humidity10'
        db.delete_column('cronos_weatherdatapoint', 'humidity10')

        # Deleting field 'WeatherDataPoint.wind_speed2'
        db.delete_column('cronos_weatherdatapoint', 'wind_speed2')

        # Deleting field 'WeatherDataPoint.wind_gust'
        db.delete_column('cronos_weatherdatapoint', 'wind_gust')

        # Deleting field 'WeatherDataPoint.solar_radiation'
        db.delete_column('cronos_weatherdatapoint', 'solar_radiation')

        # Deleting field 'WeatherDataPoint.photosynthetically_active_radiation'
        db.delete_column('cronos_weatherdatapoint', 'photosynthetically_active_radiation')

        # Deleting field 'WeatherDataPoint.soil_temperature'
        db.delete_column('cronos_weatherdatapoint', 'soil_temperature')

        # Deleting field 'WeatherDataPoint.soil_moisture'
        db.delete_column('cronos_weatherdatapoint', 'soil_moisture')

        # Deleting field 'WeatherDataPoint.leaf_wetness'
        db.delete_column('cronos_weatherdatapoint', 'leaf_wetness')


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
            'barometric_pressure': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'cloud_cover': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'distance_from_collar': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'humidity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'humidity10': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leaf_wetness': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'photosynthetically_active_radiation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'soil_moisture': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'soil_temperature': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'solar_radiation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cronos.Station']", 'null': 'True', 'blank': 'True'}),
            'temperature': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'temperature10': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'visibility': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'wind_direction': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'wind_gust': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'wind_speed': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'wind_speed2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'})
        }
    }

    complete_apps = ['cronos']
