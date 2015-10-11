from django.db.models import Model, CharField, FloatField, TextField, IntegerField
from django.contrib.auth.models import User #AbstractBaseUser, UserManager
from django.conf import settings
from django.db.models.signals import post_save, pre_init
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from app1.utils import LogHandler
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
    gs = FloatField('GS', default = DEFAULT_NUM)
    team = CharField('Team', max_length = MAX_CHAR_LENGTH, default = '')
    season = CharField('Season', max_length = MAX_CHAR_LENGTH, default = '')
    url = CharField('URL', max_length = 300, default = '')
    def __unicode__(self):
       return '%s %s' % (self.name, self.season)

class Player(Model):
    name = CharField('Name', max_length = MAX_CHAR_LENGTH, default = '')
    image = TextField(default = DEFAULT_PIC_NOT_FOUND)
    draft_year = IntegerField('Draft Year', default = DEFAULT_NUM)
    position = CharField('Position', max_length = MAX_CHAR_LENGTH, default = '')
    height = CharField('Height', max_length = MAX_CHAR_LENGTH, default = '')
    height_inches = IntegerField('Height (in)', default = DEFAULT_NUM)
    weight = CharField('Weight', max_length = MAX_CHAR_LENGTH, default = '')
    weight_lb = IntegerField('Weight (lb)', default = DEFAULT_NUM)
    url = CharField('URL', max_length = MAX_CHAR_LENGTH, default = '')
    def __unicode__(self):
        return self.name