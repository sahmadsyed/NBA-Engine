# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Stats'
        db.delete_table('app1_stats')


    def backwards(self, orm):
        # Adding model 'Stats'
        db.create_table('app1_stats', (
            ('gp', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('bpg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('tfg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('ft', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('mpg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('rpg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('spg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('ppg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('fg', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal('app1', ['Stats'])


    models = {
        'app1.player': {
            'Meta': {'object_name': 'Player'},
            'draft_year': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'stats': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app1.Statistics']", 'null': 'True'}),
            'team_city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'team_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'app1.statistics': {
            'Meta': {'object_name': 'Statistics'},
            'apg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bpg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'fg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'ft': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'gp': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'ppg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'rpg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'spg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'tfg': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['app1']