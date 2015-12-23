from requests import get
from logging import ERROR
from app1.models import PlayerID, Player
from app1.utils import LogHandler

URL = 'http://stats.nba.com/stats/commonplayerinfo'
LEAGUE_ID = '00'
SEASON_TYPE = 'Regular Season'
URL_IMAGE = 'http://stats.nba.com/media/players/230x185/%d.png'
LOGGER = LogHandler(__name__)

def get_player_info():
	player_ids = [p.player_id for p in PlayerID.objects.all()]
	params_ = {'LeagueID' : LEAGUE_ID, 'SeasonType' : SEASON_TYPE}
	Player.objects.all().delete()
	count = 1
	for play_id in player_ids:
		try:
			params_['PlayerID'] = play_id
			request = get(URL, params=params_).json()
			info_list = request['resultSets'][0]['rowSet'][0]

			info = Player()
			info.name = info_list[3]
			info.number = info_list[13]
			info.image = URL_IMAGE % play_id
			info.year_enter_league = info_list[22]
			info.position = info_list[14]
			info.height = info_list[10]
			info.weight = info_list[11]
			info.current_team = '%s %s' % (info_list[20], info_list[17])
			info.player_id = play_id
			info.save()
			print count, info.name
			count += 1
		except Exception, e:
			LOGGER.log(ERROR, 'Player Info Error')
			LOGGER.log(ERROR, 'ID: %d' % play_id)
			LOGGER.log(ERROR, 'Error: %s' % e)