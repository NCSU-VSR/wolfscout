# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Animal.date'
        db.add_column('wildlife_animal', 'date', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.time'
        db.add_column('wildlife_animal', 'time', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.location'
        db.add_column('wildlife_animal', 'location', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.trap'
        db.add_column('wildlife_animal', 'trap', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.crowntorump'
        db.add_column('wildlife_animal', 'crowntorump', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.chest'
        db.add_column('wildlife_animal', 'chest', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.neck'
        db.add_column('wildlife_animal', 'neck', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.weight'
        db.add_column('wildlife_animal', 'weight', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.hair'
        db.add_column('wildlife_animal', 'hair', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Animal.ticks'
        db.add_column('wildlife_animal', 'ticks', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Animal.feces'
        db.add_column('wildlife_animal', 'feces', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Animal.status'
        db.add_column('wildlife_animal', 'status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Animal.date'
        db.delete_column('wildlife_animal', 'date')

        # Deleting field 'Animal.time'
        db.delete_column('wildlife_animal', 'time')

        # Deleting field 'Animal.location'
        db.delete_column('wildlife_animal', 'location')

        # Deleting field 'Animal.trap'
        db.delete_column('wildlife_animal', 'trap')

        # Deleting field 'Animal.crowntorump'
        db.delete_column('wildlife_animal', 'crowntorump')

        # Deleting field 'Animal.chest'
        db.delete_column('wildlife_animal', 'chest')

        # Deleting field 'Animal.neck'
        db.delete_column('wildlife_animal', 'neck')

        # Deleting field 'Animal.weight'
        db.delete_column('wildlife_animal', 'weight')

        # Deleting field 'Animal.hair'
        db.delete_column('wildlife_animal', 'hair')

        # Deleting field 'Animal.ticks'
        db.delete_column('wildlife_animal', 'ticks')

        # Deleting field 'Animal.feces'
        db.delete_column('wildlife_animal', 'feces')

        # Deleting field 'Animal.status'
        db.delete_column('wildlife_animal', 'status')


    models = {
        'gpscollar.collar': {
            'Meta': {'object_name': 'Collar'},
            'collarID': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'wildlife.animal': {
            'Meta': {'object_name': 'Animal'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'blood': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'chest': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'collar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gpscollar.Collar']", 'null': 'True', 'blank': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'crowntorump': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'feces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hair': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'neck': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wildlife.Species']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ticks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'trap': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'})
        },
        'wildlife.species': {
            'Meta': {'object_name': 'Species'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['wildlife']
