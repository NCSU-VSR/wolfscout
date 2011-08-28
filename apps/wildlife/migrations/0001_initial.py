# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'collar'
        db.create_table('wildlife_collar', (
            ('collar_ID', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
        ))
        db.send_create_signal('wildlife', ['collar'])

        # Adding model 'collar_data'
        db.create_table('wildlife_collar_data', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collar_ID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wildlife.collar'])),
            ('GMT_DATETIME', self.gf('django.db.models.fields.DateTimeField')()),
            ('LMT_DATETIME', self.gf('django.db.models.fields.DateTimeField')()),
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
        ))
        db.send_create_signal('wildlife', ['collar_data'])

        # Adding model 'species'
        db.create_table('wildlife_species', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('wildlife', ['species'])

        # Adding model 'specimen'
        db.create_table('wildlife_specimen', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collar_ID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wildlife.collar'], null=True, blank=True)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wildlife.species'], null=True, blank=True)),
        ))
        db.send_create_signal('wildlife', ['specimen'])


    def backwards(self, orm):
        
        # Deleting model 'collar'
        db.delete_table('wildlife_collar')

        # Deleting model 'collar_data'
        db.delete_table('wildlife_collar_data')

        # Deleting model 'species'
        db.delete_table('wildlife_species')

        # Deleting model 'specimen'
        db.delete_table('wildlife_specimen')


    models = {
        'wildlife.collar': {
            'Meta': {'object_name': 'collar'},
            'collar_ID': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'wildlife.collar_data': {
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
            'DOP': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'ECEF_X': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ECEF_Y': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ECEF_Z': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'GMT_DATETIME': ('django.db.models.fields.DateTimeField', [], {}),
            'HEIGHT': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'LATITUDE': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'LMT_DATETIME': ('django.db.models.fields.DateTimeField', [], {}),
            'LONGITUDE': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
            'MAIN_VOL': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'Meta': {'object_name': 'collar_data'},
            'REMARKS': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'SATS_USED': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'TEMP': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'VALIDATED': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'collar_ID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wildlife.collar']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wildlife.species': {
            'Meta': {'object_name': 'species'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'wildlife.specimen': {
            'Meta': {'object_name': 'specimen'},
            'collar_ID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wildlife.collar']", 'null': 'True', 'blank': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wildlife.species']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['wildlife']
