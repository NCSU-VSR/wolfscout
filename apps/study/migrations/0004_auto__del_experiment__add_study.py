# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Experiment'
        db.delete_table('study_experiment')

        # Removing M2M table for field collars on 'Experiment'
        db.delete_table('study_experiment_collars')

        # Removing M2M table for field members on 'Experiment'
        db.delete_table('study_experiment_members')

        # Adding model 'Study'
        db.create_table('study_study', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('last_accessed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 10, 31, 10, 19, 15, 57311), null=True, blank=True)),
        ))
        db.send_create_signal('study', ['Study'])

        # Adding M2M table for field collars on 'Study'
        db.create_table('study_study_collars', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('study', models.ForeignKey(orm['study.study'], null=False)),
            ('collar', models.ForeignKey(orm['gpscollar.collar'], null=False))
        ))
        db.create_unique('study_study_collars', ['study_id', 'collar_id'])

        # Adding M2M table for field members on 'Study'
        db.create_table('study_study_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('study', models.ForeignKey(orm['study.study'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('study_study_members', ['study_id', 'user_id'])


    def backwards(self, orm):
        
        # Adding model 'Experiment'
        db.create_table('study_experiment', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('last_accessed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 10, 24, 9, 58, 21, 915037), null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('study', ['Experiment'])

        # Adding M2M table for field collars on 'Experiment'
        db.create_table('study_experiment_collars', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('experiment', models.ForeignKey(orm['study.experiment'], null=False)),
            ('collar', models.ForeignKey(orm['gpscollar.collar'], null=False))
        ))
        db.create_unique('study_experiment_collars', ['experiment_id', 'collar_id'])

        # Adding M2M table for field members on 'Experiment'
        db.create_table('study_experiment_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('experiment', models.ForeignKey(orm['study.experiment'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('study_experiment_members', ['experiment_id', 'user_id'])

        # Deleting model 'Study'
        db.delete_table('study_study')

        # Removing M2M table for field collars on 'Study'
        db.delete_table('study_study_collars')

        # Removing M2M table for field members on 'Study'
        db.delete_table('study_study_members')


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
        'gpscollar.collar': {
            'Meta': {'object_name': 'Collar'},
            'collarID': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'study.study': {
            'Meta': {'object_name': 'Study'},
            'collars': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'collarsForStudy'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['gpscollar.Collar']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_accessed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 10, 31, 10, 19, 15, 57311)', 'null': 'True', 'blank': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'membersForStudy'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['study']
