from django.db.models import Model, CharField, FloatField, TextField, IntegerField, URLField
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save, pre_init
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from utils import LogHandler
from logging import DEBUG as d


MAX_CHAR_LENGTH = 500
DEFAULT_NUM = 0
DEFAULT_PIC_NOT_FOUND = 'http://i.imgur.com/3FJGY4h.jpg?1'
LOGGER = LogHandler(__name__)

class Statistics(Model):
    name = CharField('Name', max_length = MAX_CHAR_LENGTH, default = '')
    ppg = FloatField('PPG', default = DEFAULT_NUM)
    apg = FloatField('APG', default = DEFAULT_NUM)
    rpg = FloatField('RPG', default = DEFAULT_NUM)
    spg = FloatField('SPG', default = DEFAULT_NUM)
    bpg = FloatField('BPG', default = DEFAULT_NUM)
    fg = FloatField('FG%', default = DEFAULT_NUM)
    tfg = FloatField('3FG%', default = DEFAULT_NUM)
    mpg = FloatField('MPG', default = DEFAULT_NUM)
    ft = FloatField('FT%', default = DEFAULT_NUM)
    gp = FloatField('GP', default = DEFAULT_NUM)
    to = FloatField('TO', default = DEFAULT_NUM)
    team = CharField('Team', max_length = MAX_CHAR_LENGTH, default = '')
    season = CharField('Season', max_length = MAX_CHAR_LENGTH, default = '')
    player_id = IntegerField('Player ID', null=True)
    def __unicode__(self):
       return '%s %s' % (self.name, self.season)

class Player(Model):
    name = CharField('Name', max_length = MAX_CHAR_LENGTH, default = '')
    number = IntegerField('Number', null=True)
    image = TextField(default = DEFAULT_PIC_NOT_FOUND)
    year_enter_league = IntegerField('Year Entered League', null=True)
    position = CharField('Position', max_length = MAX_CHAR_LENGTH, default = '')
    height = CharField('Height', max_length = MAX_CHAR_LENGTH, default = '')
    weight = CharField('Weight', max_length = MAX_CHAR_LENGTH, default = '')
    current_team = CharField('Current Team', max_length = MAX_CHAR_LENGTH, default ='')
    player_id = IntegerField('Player ID', null=True)
    def __unicode__(self):
        return self.name

class PlayerID(Model):
    player_id = IntegerField('Player ID', null=True)
    def __int__(self):
        return self.player_id
