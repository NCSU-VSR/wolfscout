# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'WeatherDataPoint'
        db.create_table('cronos_weatherdatapoint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('temperature', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True)),
            ('humidity', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True)),
            ('barometric_pressure', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True)),
            ('precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True)),
            ('wind_speed', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True)),
            ('wind_direction', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True)),
            ('distance_from_collar', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True)),
            ('cloud_cover', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True)),
            ('visibility', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True)),
            ('sunrise', self.gf('django.db.models.fields.DateTimeField')()),
            ('sunset', self.gf('django.db.models.fields.DateTimeField')()),
            ('heat_index', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True)),
            ('extreme_events', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('cronos', ['WeatherDataPoint'])

        # Adding model 'Station'
        db.create_table('cronos_station', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('LOCATION', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('network', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('huc', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('climatedir', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('cronos', ['Station'])


    def backwards(self, orm):
        
        # Deleting model 'WeatherDataPoint'
        db.delete_table('cronos_weatherdatapoint')

        # Deleting model 'Station'
        db.delete_table('cronos_station')


    models = {
        'cronos.station': {
            'LOCATION': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'Meta': {'object_name': 'Station'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'climatedir': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'huc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'network': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
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
            'sunrise': ('django.db.models.fields.DateTimeField', [], {}),
            'sunset': ('django.db.models.fields.DateTimeField', [], {}),
            'temperature': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'visibility': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'wind_direction': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'wind_speed': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'})
        }
    }

    complete_apps = ['cronos']
