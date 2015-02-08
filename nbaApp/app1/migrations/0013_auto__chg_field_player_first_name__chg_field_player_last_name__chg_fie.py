# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Player.first_name'
        db.alter_column(u'app1_player', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Player.last_name'
        db.alter_column(u'app1_player', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Player.weight'
        db.alter_column(u'app1_player', 'weight', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Player.height'
        db.alter_column(u'app1_player', 'height', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Player.position'
        db.alter_column(u'app1_player', 'position', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Statistics.first_name'
        db.alter_column(u'app1_statistics', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Statistics.last_name'
        db.alter_column(u'app1_statistics', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Statistics.season'
        db.alter_column(u'app1_statistics', 'season', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Statistics.team'
        db.alter_column(u'app1_statistics', 'team', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'Player.first_name'
        db.alter_column(u'app1_player', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Player.last_name'
        db.alter_column(u'app1_player', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Player.weight'
        db.alter_column(u'app1_player', 'weight', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Player.height'
        db.alter_column(u'app1_player', 'height', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Player.position'
        db.alter_column(u'app1_player', 'position', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Statistics.first_name'
        db.alter_column(u'app1_statistics', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Statistics.last_name'
        db.alter_column(u'app1_statistics', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Statistics.season'
        db.alter_column(u'app1_statistics', 'season', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Statistics.team'
        db.alter_column(u'app1_statistics', 'team', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        u'app1.player': {
            'Meta': {'object_name': 'Player'},
            'draft_year': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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