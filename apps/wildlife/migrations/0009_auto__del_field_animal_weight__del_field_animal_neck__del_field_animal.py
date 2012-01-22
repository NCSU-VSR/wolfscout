# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Animal.weight'
        db.delete_column('wildlife_animal', 'weight')

        # Deleting field 'Animal.neck'
        db.delete_column('wildlife_animal', 'neck')

        # Deleting field 'Animal.chest'
        db.delete_column('wildlife_animal', 'chest')

        # Deleting field 'Animal.crowntorump'
        db.delete_column('wildlife_animal', 'crowntorump')

        # Adding field 'Animal.collar_frequency'
        db.add_column('wildlife_animal', 'collar_frequency', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.crowntorump_cm'
        db.add_column('wildlife_animal', 'crowntorump_cm', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.chest_cm'
        db.add_column('wildlife_animal', 'chest_cm', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.neck_cm'
        db.add_column('wildlife_animal', 'neck_cm', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.weight_Kg'
        db.add_column('wildlife_animal', 'weight_Kg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.shooter'
        db.add_column('wildlife_animal', 'shooter', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.frequency_VIT'
        db.add_column('wildlife_animal', 'frequency_VIT', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.antennaLength_VIT'
        db.add_column('wildlife_animal', 'antennaLength_VIT', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.shotGPS'
        db.add_column('wildlife_animal', 'shotGPS', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.recoveryGPS'
        db.add_column('wildlife_animal', 'recoveryGPS', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.flightDist'
        db.add_column('wildlife_animal', 'flightDist', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.recovery_min'
        db.add_column('wildlife_animal', 'recovery_min', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.drugMix'
        db.add_column('wildlife_animal', 'drugMix', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.estAge'
        db.add_column('wildlife_animal', 'estAge', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Animal.weight'
        db.add_column('wildlife_animal', 'weight', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.neck'
        db.add_column('wildlife_animal', 'neck', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.chest'
        db.add_column('wildlife_animal', 'chest', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Adding field 'Animal.crowntorump'
        db.add_column('wildlife_animal', 'crowntorump', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=5, blank=True), keep_default=False)

        # Deleting field 'Animal.collar_frequency'
        db.delete_column('wildlife_animal', 'collar_frequency')

        # Deleting field 'Animal.crowntorump_cm'
        db.delete_column('wildlife_animal', 'crowntorump_cm')

        # Deleting field 'Animal.chest_cm'
        db.delete_column('wildlife_animal', 'chest_cm')

        # Deleting field 'Animal.neck_cm'
        db.delete_column('wildlife_animal', 'neck_cm')

        # Deleting field 'Animal.weight_Kg'
        db.delete_column('wildlife_animal', 'weight_Kg')

        # Deleting field 'Animal.shooter'
        db.delete_column('wildlife_animal', 'shooter')

        # Deleting field 'Animal.frequency_VIT'
        db.delete_column('wildlife_animal', 'frequency_VIT')

        # Deleting field 'Animal.antennaLength_VIT'
        db.delete_column('wildlife_animal', 'antennaLength_VIT')

        # Deleting field 'Animal.shotGPS'
        db.delete_column('wildlife_animal', 'shotGPS')

        # Deleting field 'Animal.recoveryGPS'
        db.delete_column('wildlife_animal', 'recoveryGPS')

        # Deleting field 'Animal.flightDist'
        db.delete_column('wildlife_animal', 'flightDist')

        # Deleting field 'Animal.recovery_min'
        db.delete_column('wildlife_animal', 'recovery_min')

        # Deleting field 'Animal.drugMix'
        db.delete_column('wildlife_animal', 'drugMix')

        # Deleting field 'Animal.estAge'
        db.delete_column('wildlife_animal', 'estAge')


    models = {
        'gpscollar.collar': {
            'Meta': {'object_name': 'Collar'},
            'collarID': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'wildlife.animal': {
            'Meta': {'object_name': 'Animal'},
            'age_class': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'antennaLength_VIT': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'blood': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'chest_cm': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'collar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gpscollar.Collar']", 'null': 'True', 'blank': 'True'}),
            'collar_frequency': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'common_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'crowntorump_cm': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'drugMix': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'estAge': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'feces': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flightDist': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'frequency_VIT': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'hair': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'neck_cm': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'recoveryGPS': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'recovery_min': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'shooter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'shotGPS': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wildlife.Species']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ticks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'trap': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'weight_Kg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'})
        },
        'wildlife.species': {
            'Meta': {'object_name': 'Species'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['wildlife']
