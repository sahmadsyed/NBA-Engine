# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Statistics'
        db.create_table(u'main_statistics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ppg', self.gf('django.db.models.fields.FloatField')()),
            ('apg', self.gf('django.db.models.fields.FloatField')()),
            ('rpg', self.gf('django.db.models.fields.FloatField')()),
            ('spg', self.gf('django.db.models.fields.FloatField')()),
            ('bpg', self.gf('django.db.models.fields.FloatField')()),
            ('fg', self.gf('django.db.models.fields.FloatField')()),
            ('tfg', self.gf('django.db.models.fields.FloatField')()),
            ('mpg', self.gf('django.db.models.fields.FloatField')()),
            ('ft', self.gf('django.db.models.fields.FloatField')()),
            ('gp', self.gf('django.db.models.fields.FloatField')()),
            ('topg', self.gf('django.db.models.fields.FloatField')()),
            ('team', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('season', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['Statistics'])

        # Adding model 'Player'
        db.create_table(u'main_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('image', self.gf('django.db.models.fields.URLField')(default='', max_length=200)),
            ('year_enter_league', self.gf('django.db.models.fields.IntegerField')()),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('weight', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('current_team', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['Player'])

        # Adding model 'PlayerID'
        db.create_table(u'main_playerid', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'main', ['PlayerID'])


    def backwards(self, orm):
        # Deleting model 'Statistics'
        db.delete_table(u'main_statistics')

        # Deleting model 'Player'
        db.delete_table(u'main_player')

        # Deleting model 'PlayerID'
        db.delete_table(u'main_playerid')


    models = {
        u'main.player': {
            'Meta': {'object_name': 'Player'},
            'current_team': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'player_id': ('django.db.models.fields.IntegerField', [], {}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year_enter_league': ('django.db.models.fields.IntegerField', [], {})
        },
        u'main.playerid': {
            'Meta': {'object_name': 'PlayerID'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'main.statistics': {
            'Meta': {'object_name': 'Statistics'},
            'apg': ('django.db.models.fields.FloatField', [], {}),
            'bpg': ('django.db.models.fields.FloatField', [], {}),
            'fg': ('django.db.models.fields.FloatField', [], {}),
            'ft': ('django.db.models.fields.FloatField', [], {}),
            'gp': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpg': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'player_id': ('django.db.models.fields.IntegerField', [], {}),
            'ppg': ('django.db.models.fields.FloatField', [], {}),
            'rpg': ('django.db.models.fields.FloatField', [], {}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'spg': ('django.db.models.fields.FloatField', [], {}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tfg': ('django.db.models.fields.FloatField', [], {}),
            'topg': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['main']