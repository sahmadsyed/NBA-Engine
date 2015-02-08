# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stats'
        db.create_table('app1_stats', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ppg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('apg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('rpg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('spg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('bpg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('fg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('tfg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('mpg', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('ft', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('gp', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal('app1', ['Stats'])

        # Adding model 'Player'
        db.create_table('app1_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('draft_year', self.gf('django.db.models.fields.IntegerField')()),
            ('team_city', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('team_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('app1', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Stats'
        db.delete_table('app1_stats')

        # Deleting model 'Player'
        db.delete_table('app1_player')


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