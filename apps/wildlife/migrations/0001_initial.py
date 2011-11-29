# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Species'
        db.create_table('wildlife_species', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('wildlife', ['Species'])

        # Adding model 'Specimen'
        db.create_table('wildlife_specimen', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gpscollar.Collar'], null=True, blank=True)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wildlife.Species'], null=True, blank=True)),
        ))
        db.send_create_signal('wildlife', ['Specimen'])


    def backwards(self, orm):
        
        # Deleting model 'Species'
        db.delete_table('wildlife_species')

        # Deleting model 'Specimen'
        db.delete_table('wildlife_specimen')


    models = {
        'gpscollar.collar': {
            'Meta': {'object_name': 'Collar'},
            'collarID': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'wildlife.species': {
            'Meta': {'object_name': 'Species'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'wildlife.specimen': {
            'Meta': {'object_name': 'Specimen'},
            'collar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gpscollar.Collar']", 'null': 'True', 'blank': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wildlife.Species']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['wildlife']
