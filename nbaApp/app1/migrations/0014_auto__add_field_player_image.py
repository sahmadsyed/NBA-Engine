# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Player.image'
        db.add_column(u'app1_player', 'image',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Player.image'
        db.delete_column(u'app1_player', 'image')


    models = {
        u'app1.player': {
            'Meta': {'object_name': 'Player'},
            'draft_year': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            'weight': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'})
        },
        u'app1.statistics': {
            'Meta': {'object_name': 'Statistics'},
            'apg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'bpg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'fg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            'ft': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'gp': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'gs': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            'mpg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'ppg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'rpg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'season': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            'spg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'team': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            'tfg': ('django.db.models.fields.FloatField', [], {'default': '-1'})
        }
    }

    complete_apps = ['app1']