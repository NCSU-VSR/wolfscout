# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Station.end_date'
        db.delete_column('cronos_station', 'end_date')

        # Deleting field 'Station.active'
        db.delete_column('cronos_station', 'active')

        # Deleting field 'Station.climatedir'
        db.delete_column('cronos_station', 'climatedir')

        # Deleting field 'Station.country'
        db.delete_column('cronos_station', 'country')

        # Deleting field 'Station.start_date'
        db.delete_column('cronos_station', 'start_date')

        # Adding field 'Station.elevation'
        db.add_column('cronos_station', 'elevation', self.gf('django.db.models.fields.DecimalField')(default=100.2, max_digits=12, decimal_places=2), keep_default=False)

        # Adding field 'Station.county'
        db.add_column('cronos_station', 'county', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'Station.climatediv'
        db.add_column('cronos_station', 'climatediv', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Station.end_date'
        db.add_column('cronos_station', 'end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'Station.active'
        db.add_column('cronos_station', 'active', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Adding field 'Station.climatedir'
        db.add_column('cronos_station', 'climatedir', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'Station.country'
        db.add_column('cronos_station', 'country', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'Station.start_date'
        db.add_column('cronos_station', 'start_date', self.gf('django.db.models.fields.DateField')(default=datetime.date(2011, 11, 9)), keep_default=False)

        # Deleting field 'Station.elevation'
        db.delete_column('cronos_station', 'elevation')

        # Deleting field 'Station.county'
        db.delete_column('cronos_station', 'county')

        # Deleting field 'Station.climatediv'
        db.delete_column('cronos_station', 'climatediv')


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
        }
    }

    complete_apps = ['cronos']
