# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Player.stats'
        db.alter_column('app1_player', 'stats_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['app1.Stats']))

    def backwards(self, orm):

        # Changing field 'Player.stats'
        db.alter_column('app1_player', 'stats_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app1.Stats']))

    models = {
        'app1.player': {
            'Meta': {'object_name': 'Player'},
            'draft_year': ('django.db.models.fields.IntegerField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'stats': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['app1.Stats']"}),
            'team_city': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
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