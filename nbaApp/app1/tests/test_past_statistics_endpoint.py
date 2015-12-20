import requests
from app1.utils import LogHandler
from app1.tests.base_endpoint_tests import BaseEndpointTests

LOGGER = LogHandler(__name__)


class PastStatisticsEndpointTests(BaseEndpointTests):
	URL = 'http://127.0.0.1:8000/player_list/api/past_statistics/'

	def test_all_fields_present(self):
		params_ = {'name' : 'Chris Bosh'}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		r = response.json()
		self.assertIn('stats', r)
		self.assertIn('count', r)
		stats = r['stats']
		for stat in stats:
			self.assertIn('id', stat)
			self.assertIn('name', stat)
			self.assertIn('ppg', stat)
			self.assertIn('apg', stat)
			self.assertIn('rpg', stat)
			self.assertIn('spg', stat)
			self.assertIn('bpg', stat)
			self.assertIn('fg', stat)
			self.assertIn('tfg', stat)
			self.assertIn('mpg', stat)
			self.assertIn('ft', stat)
			self.assertIn('gp', stat)
			self.assertIn('to', stat)
			self.assertIn('team', stat)
			self.assertIn('season', stat)

	def test_with_name_and_season(self):
		params_ = {'name': 'Chris Bosh', 'season' : 2005}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)
		self.assertEqual(response.json()['count'], 1)

	def test_with_alpha_season(self):
		params_ = {'name': 'Chris Bosh', 'season' : 'season'}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.BAD)
		r = response.json()['error']
		self.assertEqual(r['status_code'], requests.codes.BAD)
		self.assertEqual(r['message'], 'Season must be a positive integer')

	def test_with_ancient_season(self):
		params_ = {'name': 'Chris Bosh', 'season' : 500}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)
		self.assertEqual(response.json()['count'], 0)
		self.assertEqual(response.json()['stats'], [])

	def test_with_no_params(self):
		response = requests.get(self.URL, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.BAD)
		r = response.json()['error']
		self.assertEqual(r['status_code'], requests.codes.BAD)
		self.assertEqual(r['message'], "Missing 'name'")