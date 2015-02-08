from django.db import models

MAX_CHAR_LENGTH = 50
DEFAULT_NUM = -1
DEFAULT_CHAR = 'DEFAULT'

class Statistics(models.Model):
    first_name = models.CharField('First Name', max_length = MAX_CHAR_LENGTH, default = DEFAULT_CHAR)
    last_name = models.CharField('Last Name', max_length = MAX_CHAR_LENGTH, default = DEFAULT_CHAR)
    ppg = models.FloatField('PPG', default = DEFAULT_NUM)
    apg = models.FloatField('APG', default = DEFAULT_NUM)
    rpg = models.FloatField('RPG', default = DEFAULT_NUM)
    spg = models.FloatField('SPG', default = DEFAULT_NUM)
    bpg = models.FloatField('BPG', default = DEFAULT_NUM)
    fg = models.FloatField('FG%', default = DEFAULT_NUM)
    tfg = models.FloatField('3FG%', default = DEFAULT_NUM)
    mpg = models.FloatField('MPG', default = DEFAULT_NUM)
    ft = models.FloatField('FT%', default = DEFAULT_NUM)
    gp = models.FloatField('GP', default = DEFAULT_NUM)
    gs = models.FloatField('GS', default = DEFAULT_NUM)
    team = models.CharField('Team', max_length = MAX_CHAR_LENGTH, default = DEFAULT_CHAR)
    season = models.CharField('Season', max_length = MAX_CHAR_LENGTH, default = DEFAULT_CHAR)
    def __unicode__(self):
       return('%s %s %s' % (self.first_name, self.last_name, self.season))

class Player(models.Model):
    #stats = models.ForeignKey(Statistics, null=True)
    first_name = models.CharField('First Name', max_length = MAX_CHAR_LENGTH, default = DEFAULT_CHAR)
    last_name = models.CharField('Last Name', max_length = MAX_CHAR_LENGTH, default = DEFAULT_CHAR)
    image = models.TextField(default = '')
    draft_year = models.IntegerField('Draft Year', default = DEFAULT_NUM)
    position = models.CharField('Position', max_length = MAX_CHAR_LENGTH, default = DEFAULT_CHAR)
    height = models.CharField('Height', max_length = MAX_CHAR_LENGTH, default = DEFAULT_CHAR)
    weight = models.CharField('Weight', max_length = MAX_CHAR_LENGTH, default = DEFAULT_CHAR)
    def __unicode__(self):
        return('%s %s' % (self.first_name, self.last_name))

