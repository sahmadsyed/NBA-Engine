# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Statistics.gs'
        db.delete_column(u'app1_statistics', 'gs')

        # Adding field 'Statistics.to'
        db.add_column(u'app1_statistics', 'to',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Statistics.gs'
        db.add_column(u'app1_statistics', 'gs',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Deleting field 'Statistics.to'
        db.delete_column(u'app1_statistics', 'to')


    models = {
        u'app1.player': {
            'Meta': {'object_name': 'Player'},
            'draft_year': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'height_inches': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'default': "'http://i.imgur.com/3FJGY4h.jpg?1'"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'weight': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'weight_lb': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'app1.statistics': {
            'Meta': {'object_name': 'Statistics'},
            'apg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bpg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'fg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'ft': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'gp': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'ppg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'rpg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'season': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'spg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'team': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'tfg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'to': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'})
        }
    }

    complete_apps = ['app1']