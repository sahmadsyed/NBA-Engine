from logging import ERROR, INFO
from requests import get

from cacheback.base import Job

from main.models import PlayerID
from utils import LogHandler, get_current_season


# constants
LEAGUE_ID = '00'
PER_MODE = 'PerGame'
STATS_URL = 'http://stats.nba.com/stats/playercareerstats'
LOGGER = LogHandler(__name__)

class CurrentSeasonStatsJob(Job):
    lifetime = 86400
    fetch_on_miss = True

    def fetch(self):
        player_ids = [p.player_id for p in PlayerID.objects.all()]
        params_ = {'LeagueID' : LEAGUE_ID, 'PerMode' : PER_MODE}
        current_season_stats = []
        LOGGER.log(INFO,'Caching........')
        for play_id in player_ids:
            try:
                params_['PlayerID'] = play_id
                request = get(STATS_URL, params=params_).json()
                name_ = Player.objects.get(player_id=play_id).name
                stats_list = request['resultSets'][0]['rowSet']
                current_season = get_current_season()
                current_stats = [i for i in dropwhile(lambda s: s[1] != current_season, stats_list)]

                if current_stats:
                    stat = current_stats[-1]
                    stats = Statistics()
                    stats.name = name_
                    stats.ppg = stat[26]
                    stats.apg = stat[21]
                    stats.rpg = stat[20]
                    stats.spg = stat[22]
                    stats.bpg = stat[23]
                    stats.fg = stat[11]
                    stats.tfg = stat[14]
                    stats.mpg = stat[8]
                    stats.ft = stat[17]
                    stats.gp = stat[6]
                    stats.topg = stat[24]
                    stats.season = stat[1]
                    stats.player_id = play_id

                    # gets correct team in case traded mid-season
                    if stat[4] == 'TOT':
                        stats.team = current_stats[-2][4]
                    else:
                        stats.team = stat[4]

                    current_season_stats.append(stats)
                    LOGGER.log(INFO, 'Cached: %s' % name_)
            except Exception, e:
                LOGGER.log(ERROR, 'Caching Error')
                LOGGER.log(ERROR, 'ID: %d' % play_id)
                LOGGER.log(ERROR, 'Error: %s' % e)
        return current_season_stats

    def should_stale_item_be_fetched_synchronously(self, delta):
        return False
