# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PlayerURL'
        db.delete_table(u'app1_playerurl')

        # Deleting field 'Player.height_inches'
        db.delete_column(u'app1_player', 'height_inches')

        # Deleting field 'Player.url'
        db.delete_column(u'app1_player', 'url')

        # Deleting field 'Player.draft_year'
        db.delete_column(u'app1_player', 'draft_year')

        # Deleting field 'Player.weight_lb'
        db.delete_column(u'app1_player', 'weight_lb')

        # Adding field 'Player.number'
        db.add_column(u'app1_player', 'number',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Player.year_enter_league'
        db.add_column(u'app1_player', 'year_enter_league',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Player.current_team'
        db.add_column(u'app1_player', 'current_team',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)

        # Adding field 'Player.player_id'
        db.add_column(u'app1_player', 'player_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Deleting field 'Statistics.url'
        db.delete_column(u'app1_statistics', 'url')

        # Adding field 'Statistics.player_id'
        db.add_column(u'app1_statistics', 'player_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'PlayerURL'
        db.create_table(u'app1_playerurl', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length=500)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'app1', ['PlayerURL'])

        # Adding field 'Player.height_inches'
        db.add_column(u'app1_player', 'height_inches',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.url'
        db.add_column(u'app1_player', 'url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)

        # Adding field 'Player.draft_year'
        db.add_column(u'app1_player', 'draft_year',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.weight_lb'
        db.add_column(u'app1_player', 'weight_lb',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Player.number'
        db.delete_column(u'app1_player', 'number')

        # Deleting field 'Player.year_enter_league'
        db.delete_column(u'app1_player', 'year_enter_league')

        # Deleting field 'Player.current_team'
        db.delete_column(u'app1_player', 'current_team')

        # Deleting field 'Player.player_id'
        db.delete_column(u'app1_player', 'player_id')

        # Adding field 'Statistics.url'
        db.add_column(u'app1_statistics', 'url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300),
                      keep_default=False)

        # Deleting field 'Statistics.player_id'
        db.delete_column(u'app1_statistics', 'player_id')


    models = {
        u'app1.player': {
            'Meta': {'object_name': 'Player'},
            'current_team': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'default': "'http://i.imgur.com/3FJGY4h.jpg?1'"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'player_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'weight': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'year_enter_league': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'app1.playerid': {
            'Meta': {'object_name': 'PlayerID'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player_id': ('django.db.models.fields.IntegerField', [], {})
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
            'player_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'ppg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'rpg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'season': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'spg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'team': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'tfg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'to': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['app1']