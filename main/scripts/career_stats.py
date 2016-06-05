from requests import get
from logging import ERROR
from main.models import Statistics, PlayerID, Player
from utils import LogHandler, get_current_season

URL = 'http://stats.nba.com/stats/playercareerstats'
LEAGUE_ID = '00'
PER_MODE = 'PerGame'
LOGGER = LogHandler(__name__)


def get_career_stats():
	player_ids = [p.player_id for p in PlayerID.objects.all()]
	params_ = {'LeagueID' : LEAGUE_ID, 'PerMode' : PER_MODE}
	Statistics.objects.all().delete()
	count = 1
	for play_id in player_ids:
		try:
			params_['PlayerID'] = play_id
			request = get(URL, params=params_).json()
			stats_list = request['resultSets'][0]['rowSet']
			name_ = Player.objects.get(player_id=play_id).name
			current_season = get_current_season()
			stat_count = 0

			for stat in stats_list:
				stat_count+=1
				# do not save if it is current regular season stats
				if stat_count == len(stats_list) and stat[1] == current_season:
					break
				print stat[1]
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
				stats.to = stat[24]
				stats.team = stat[4]
				stats.season = stat[1]
				stats.player_id = play_id
				stats.save()
			print count, name_
			count += 1
		except Exception, e:
			LOGGER.log(ERROR, 'Career Stats Error')
			LOGGER.log(ERROR, 'ID: %d' % play_id)
			LOGGER.log(ERROR, 'Error: %s' % e)
