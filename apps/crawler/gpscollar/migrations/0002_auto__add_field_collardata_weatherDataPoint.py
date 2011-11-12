# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'CollarData.weatherDataPoint'
        db.add_column('gpscollar_collardata', 'weatherDataPoint', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cronos.WeatherDataPoint'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'CollarData.weatherDataPoint'
        db.delete_column('gpscollar_collardata', 'weatherDataPoint_id')


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
            'extreme_events': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'heat_index': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'humidity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cronos.Station']", 'null': 'True', 'blank': 'True'}),
            'sunrise': ('django.db.models.fields.DateTimeField', [], {}),
            'sunset': ('django.db.models.fields.DateTimeField', [], {}),
            'temperature': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'visibility': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'wind_direction': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'wind_speed': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'})
        },
        'gpscollar.collar': {
            'Meta': {'object_name': 'Collar'},
            'collarID': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'gpscollar.collardata': {
            'BU_VOL': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'CH10_CN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH10_SATID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH11_CN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH11_SATID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH12_CN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH12_SATID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH1_CN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH1_SATID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH2_CN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH2_SATID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH3_CN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH3_SATID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH4_CN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH4_SATID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH5_CN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH5_SATID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH6_CN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH6_SATID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH7_CN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH7_SATID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH8_CN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH8_SATID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH9_CN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'CH9_SATID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'DATE_ADDED': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 11, 12, 15, 19, 0, 308427)'}),
            'DOP': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'ECEF_X': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ECEF_Y': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ECEF_Z': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'GMT_DATETIME': ('django.db.models.fields.DateTimeField', [], {}),
            'HEIGHT': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'LATITUDE': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'LMT_DATETIME': ('django.db.models.fields.DateTimeField', [], {}),
            'LOCATION': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'LONGITUDE': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'MAIN_VOL': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'Meta': {'object_name': 'CollarData'},
            'REMARKS': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'SATS_USED': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'TEMP': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VALID': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'VALIDATED': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'collar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gpscollar.Collar']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weatherDataPoint': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cronos.WeatherDataPoint']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gpscollar']
