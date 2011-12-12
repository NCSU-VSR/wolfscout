# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ShapeInteractionGroup.time_delta'
        db.add_column('study_shapeinteractiongroup', 'time_delta', self.gf('django.db.models.fields.TimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'AnimalInteractionGroup.time_delta'
        db.add_column('study_animalinteractiongroup', 'time_delta', self.gf('django.db.models.fields.TimeField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ShapeInteractionGroup.time_delta'
        db.delete_column('study_shapeinteractiongroup', 'time_delta')

        # Deleting field 'AnimalInteractionGroup.time_delta'
        db.delete_column('study_animalinteractiongroup', 'time_delta')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cronos.station': {
            'LOCATION': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'Meta': {'object_name': 'Station'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'climatediv': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'elevation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
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
            'distance_to_station': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '7', 'blank': 'True'}),
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
            'DATE_ADDED': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 12, 11, 15, 16, 32, 71558)'}),
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
        },
        'study.animalinteraction': {
            'Meta': {'object_name': 'AnimalInteraction'},
            'destination_animal_data_point': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'AnimalDestinationOfInteraction'", 'to': "orm['gpscollar.CollarData']"}),
            'distance': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interaction_group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'AnimalInteractionGroupForInteraction'", 'null': 'True', 'to': "orm['study.AnimalInteractionGroup']"}),
            'source_animal_data_point': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'AnimalSourceOfInteraction'", 'to': "orm['gpscollar.CollarData']"})
        },
        'study.animalinteractiongroup': {
            'Meta': {'object_name': 'AnimalInteractionGroup'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dbf_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'distance': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prj_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'shp_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'shx_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'AnimalInteractionStudyGroup'", 'to': "orm['study.Study']"}),
            'time_delta': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'zip_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'study.shapeinteraction': {
            'Meta': {'object_name': 'ShapeInteraction'},
            'destination_animal_data_point': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ShapeAnimalDestinationOfInteraction'", 'to': "orm['gpscollar.CollarData']"}),
            'distance': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interaction_group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ShapeInteractionGrouppForInteraction'", 'null': 'True', 'to': "orm['study.AnimalInteractionGroup']"}),
            'source_shapes': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'AnimalSourceOfInteraction'", 'to': "orm['study.ShapeToAnalyze']"})
        },
        'study.shapeinteractiongroup': {
            'Meta': {'object_name': 'ShapeInteractionGroup'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dbf_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'distance': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '5', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prj_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'shp_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'shx_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'study': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ShapeInteractionGroup'", 'to': "orm['study.Study']"}),
            'time_delta': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'zip_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'study.shapetoanalyze': {
            'Meta': {'object_name': 'ShapeToAnalyze'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shapes': ('django.contrib.gis.db.models.fields.GeometryCollectionField', [], {'null': 'True', 'blank': 'True'})
        },
        'study.study': {
            'Meta': {'object_name': 'Study'},
            'collars': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'collarsForStudy'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['gpscollar.Collar']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_accessed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 12, 11, 15, 16, 32, 74382)', 'null': 'True', 'blank': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'membersForStudy'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['study']
