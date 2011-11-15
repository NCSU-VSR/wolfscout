# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Collar'
        db.create_table('gpscollar_collar', (
            ('collarID', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
        ))
        db.send_create_signal('gpscollar', ['Collar'])

        # Adding model 'CollarData'
        db.create_table('gpscollar_collardata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gpscollar.Collar'])),
            ('GMT_DATETIME', self.gf('django.db.models.fields.DateTimeField')()),
            ('LMT_DATETIME', self.gf('django.db.models.fields.DateTimeField')()),
            ('LOCATION', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('ECEF_X', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ECEF_Y', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ECEF_Z', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('LATITUDE', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True)),
            ('LONGITUDE', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=7, blank=True)),
            ('HEIGHT', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2, blank=True)),
            ('DOP', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('VALIDATED', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('SATS_USED', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH1_SATID', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH1_CN', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH2_SATID', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH2_CN', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH3_SATID', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH3_CN', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH4_SATID', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH4_CN', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH5_SATID', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH5_CN', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH6_SATID', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH6_CN', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH7_SATID', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH7_CN', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH8_SATID', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH8_CN', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH9_SATID', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH9_CN', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH10_SATID', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH10_CN', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH11_SATID', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH11_CN', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH12_SATID', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('CH12_CN', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('MAIN_VOL', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('BU_VOL', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('TEMP', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('REMARKS', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('VALID', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('DATE_ADDED', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 11, 12, 15, 18, 19, 740066))),
        ))
        db.send_create_signal('gpscollar', ['CollarData'])


    def backwards(self, orm):
        
        # Deleting model 'Collar'
        db.delete_table('gpscollar_collar')

        # Deleting model 'CollarData'
        db.delete_table('gpscollar_collardata')


    models = {
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
            'DATE_ADDED': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 11, 12, 15, 18, 19, 740066)'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['gpscollar']
