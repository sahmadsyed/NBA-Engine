# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Player.height_inches'
        db.add_column(u'app1_player', 'height_inches',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.weight_lb'
        db.add_column(u'app1_player', 'weight_lb',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Player.name'
        db.alter_column(u'app1_player', 'name', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Player.weight'
        db.alter_column(u'app1_player', 'weight', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Player.url'
        db.alter_column(u'app1_player', 'url', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Player.height'
        db.alter_column(u'app1_player', 'height', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Player.position'
        db.alter_column(u'app1_player', 'position', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Statistics.name'
        db.alter_column(u'app1_statistics', 'name', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Statistics.season'
        db.alter_column(u'app1_statistics', 'season', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Statistics.team'
        db.alter_column(u'app1_statistics', 'team', self.gf('django.db.models.fields.CharField')(max_length=500))

    def backwards(self, orm):
        # Deleting field 'Player.height_inches'
        db.delete_column(u'app1_player', 'height_inches')

        # Deleting field 'Player.weight_lb'
        db.delete_column(u'app1_player', 'weight_lb')


        # Changing field 'Player.name'
        db.alter_column(u'app1_player', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Player.weight'
        db.alter_column(u'app1_player', 'weight', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Player.url'
        db.alter_column(u'app1_player', 'url', self.gf('django.db.models.fields.CharField')(max_length=300))

        # Changing field 'Player.height'
        db.alter_column(u'app1_player', 'height', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Player.position'
        db.alter_column(u'app1_player', 'position', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Statistics.name'
        db.alter_column(u'app1_statistics', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Statistics.season'
        db.alter_column(u'app1_statistics', 'season', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Statistics.team'
        db.alter_column(u'app1_statistics', 'team', self.gf('django.db.models.fields.CharField')(max_length=50))

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
            'gs': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'ppg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'rpg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'season': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'spg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'team': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'tfg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'})
        }
    }

    complete_apps = ['app1']