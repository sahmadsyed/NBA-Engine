import requests
from random import shuffle
from app1.utils import LogHandler
from app1.tests.base_endpoint_tests import BaseEndpointTests
from logging import DEBUG

LOGGER = LogHandler(__name__)


class PlayersEndpointTests(BaseEndpointTests):
	URL = 'http://127.0.0.1:8000/player_list/api/players/'

	def test_all_fields_present(self):
		response = requests.get(self.URL, headers = self.VALID_HEADER)
		players = response.json()['players']
		shuffle(players)
		for player in players[:10]:
			self.assertIn('id', player)
			self.assertIn('name', player)
			self.assertIn('number', player)
			self.assertIn('image', player)
			self.assertIn('year_enter_league', player)
			self.assertIn('position', player)
			self.assertIn('height', player)
			self.assertIn('weight', player)
			self.assertIn('current_team', player)

	def test_with_name(self):
		params_ = {'name' : 'Chris Bosh'}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)
		self.assertEqual(response.json()['count'], 1)
		r = response.json()['players'][0]
		self.assertEqual(r['name'], 'Chris Bosh')
		self.assertEqual(r['number'], 1)
		self.assertEqual(r['image'], 'http://stats.nba.com/media/players/230x185/2547.png')
		self.assertEqual(r['year_enter_league'], 2003)
		self.assertEqual(r['position'], 'Forward')
		self.assertEqual(r['height'], '6-11')
		self.assertEqual(r['weight'], '235')
		self.assertEqual(r['current_team'], 'Miami Heat')

	def test_with_no_params(self):
		response = requests.get(self.URL, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)
		r = response.json()
		self.assertIn('count', r)
		self.assertIn('players', r)

	def test_with_draft_year(self):
		params_ = {'draft_year' : 2005}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)

	def test_with_position(self):
		params_ = {'position' : 'guard'}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)

	def test_with_name_position_draft_year(self):
		params_ = {'name' : 'Chris Bosh', 'draft_year' : 2003, 'position' : 'forward'}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)
		self.assertEqual(response.json()['count'], 1)
		r = response.json()['players'][0]
		self.assertEqual(r['name'], 'Chris Bosh')
		self.assertEqual(r['number'], 1)
		self.assertEqual(r['image'], 'http://stats.nba.com/media/players/230x185/2547.png')
		self.assertEqual(r['year_enter_league'], 2003)
		self.assertEqual(r['position'], 'Forward')
		self.assertEqual(r['height'], '6-11')
		self.assertEqual(r['weight'], '235')
		self.assertEqual(r['current_team'], 'Miami Heat')

	def test_with_alpha_draft_year(self):
		params_ = {'draft_year' : 'Salman Syed'}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.BAD)
		r = response.json()['error']
		self.assertEqual(r['status_code'], requests.codes.BAD)
		self.assertEqual(r['message'], 'Draft year must be a positive integer')

	def test_with_ancient_draft_year(self):
		params_ = {'draft_year' : '500'}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)
		self.assertEqual(response.json()['count'], 0)

	def test_with_invalid_position(self):
		params_ = {'position' : 'swingman'}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.not_found)
		r = response.json()['error']
		self.assertEqual(r['status_code'], requests.codes.not_found)
		self.assertEqual(r['message'], 'Incorrect position')