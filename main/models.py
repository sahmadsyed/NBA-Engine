from django.db.models import Model, CharField, FloatField, TextField, IntegerField, URLField
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save, pre_init
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from utils import LogHandler


# constants
MAX_CHAR_LENGTH = 100

class Statistics(Model):
    """
    Holds fields for basic NBA player stats.

    Attributes:
        player_id (integer): Unique id of player who these stats belong to
        name (str): Name of player who these stats belong to
        ppg (float): Points per game
        apg (float): Assists per game
        rpg (float): Rebounds per game
        spg (float): Steals per game
        bpg (float): Blocks per game
        fg (float): Field goal percentage
        tfg (float): Three point field goal percentage
        ft (float): Free throw percentage
        mpg (float): Minutes per game
        gp (float): Games played
        topg (float): Turnovers per game
        team (str): Team of player when he had these stats
        season (str): Season player had these stats

    """

    player_id = IntegerField('Player ID')
    name = CharField('Name', max_length = MAX_CHAR_LENGTH)
    ppg = FloatField('PPG')
    apg = FloatField('APG')
    rpg = FloatField('RPG')
    spg = FloatField('SPG')
    bpg = FloatField('BPG')
    fg = FloatField('FG%')
    tfg = FloatField('3FG%')
    mpg = FloatField('MPG')
    ft = FloatField('FT%')
    gp = FloatField('GP')
    topg = FloatField('TO')
    team = CharField('Team', max_length = MAX_CHAR_LENGTH)
    season = CharField('Season', max_length = MAX_CHAR_LENGTH)

    def __unicode__(self):
       return '%s %s' % (self.name, self.season)

class Player(Model):
    """
    Holds fields for basic NBA player information.

    Attributes:
        player_id (integer): Unique id of player
        name (str): Name of player
        number (integer): Number of player
        image (str): URL of player image
        year_enter_leage (integer): Year player entered league
        position (str): Position player plays
        height (str): Height of player (ft)
        weight (str): Weight of player (lbs)
        current_team (str): Name of team player currently plays for

    """

    player_id = IntegerField('Player ID')
    name = CharField('Name', max_length = MAX_CHAR_LENGTH)
    number = IntegerField('Number')
    image = URLField(default = '')
    year_enter_league = IntegerField('Year Entered League')
    position = CharField('Position', max_length = MAX_CHAR_LENGTH)
    height = CharField('Height', max_length = MAX_CHAR_LENGTH)
    weight = CharField('Weight', max_length = MAX_CHAR_LENGTH)
    current_team = CharField('Current Team', max_length = MAX_CHAR_LENGTH)

    def __unicode__(self):
        return self.name

class PlayerID(Model):
    """
    Holds unique id for NBA player

    Attributes:
        player_id (integer): Unique id of player

    """

    player_id = IntegerField('Player ID')

    def __unicode__(self):
        return unicode(self.player_id)
