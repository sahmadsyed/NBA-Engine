# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Statistics.apg'
        db.add_column('app1_statistics', 'apg',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Statistics.rpg'
        db.add_column('app1_statistics', 'rpg',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Statistics.spg'
        db.add_column('app1_statistics', 'spg',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Statistics.bpg'
        db.add_column('app1_statistics', 'bpg',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Statistics.fg'
        db.add_column('app1_statistics', 'fg',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Statistics.tfg'
        db.add_column('app1_statistics', 'tfg',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Statistics.mpg'
        db.add_column('app1_statistics', 'mpg',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Statistics.ft'
        db.add_column('app1_statistics', 'ft',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Statistics.gp'
        db.add_column('app1_statistics', 'gp',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Statistics.apg'
        db.delete_column('app1_statistics', 'apg')

        # Deleting field 'Statistics.rpg'
        db.delete_column('app1_statistics', 'rpg')

        # Deleting field 'Statistics.spg'
        db.delete_column('app1_statistics', 'spg')

        # Deleting field 'Statistics.bpg'
        db.delete_column('app1_statistics', 'bpg')

        # Deleting field 'Statistics.fg'
        db.delete_column('app1_statistics', 'fg')

        # Deleting field 'Statistics.tfg'
        db.delete_column('app1_statistics', 'tfg')

        # Deleting field 'Statistics.mpg'
        db.delete_column('app1_statistics', 'mpg')

        # Deleting field 'Statistics.ft'
        db.delete_column('app1_statistics', 'ft')

        # Deleting field 'Statistics.gp'
        db.delete_column('app1_statistics', 'gp')


    models = {
        'app1.player': {
            'Meta': {'object_name': 'Player'},
            'draft_year': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "'a'", 'max_length': '40'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "'b'", 'max_length': '40'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "'b'", 'max_length': '30'}),
            'stats': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['app1.Statistics']"}),
            'team_city': ('django.db.models.fields.CharField', [], {'default': "'a'", 'max_length': '20'}),
            'team_name': ('django.db.models.fields.CharField', [], {'default': "'b'", 'max_length': '20'}),
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
        },
        'app1.stats': {
            'Meta': {'object_name': 'Stats'},
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