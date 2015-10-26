import requests
from rest_framework.test import APITestCase
from app1.utils import LogHandler

LOGGER = LogHandler(__name__)


class PlayerEndpointTests(APITestCase):
	URL = 'http://127.0.0.1:8000/player_list/api/players/'
	VALID_HEADER = {'Authorization' : 'Token 9493289438fb1f2835e3a97b5b10dbc333ef23ff'}
	INVALID_HEADER = {'Authorization' : 'Token invalid'}

	def test_with_no_auth(self):
		response = requests.get(self.URL)
		self.assertEqual(response.status_code, requests.codes.unauthorized)

	def test_with_invalid_auth(self):
		response = requests.get(self.URL, headers = self.INVALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.unauthorized)

	def test_with_no_params(self):
		response = requests.get(self.URL, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)
		self.assertEqual(response.json()['count'], 563)

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
		self.assertEqual(r['id'], 65)

	def test_with_draft_year(self):
		params_ = {'draft_year' : 2005}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)
		self.assertEqual(response.json()['count'], 25)

	def test_with_position(self):
		params_ = {'position' : 'guard'}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)
		self.assertEqual(response.json()['count'], 205)

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
		self.assertEqual(r['id'], 65)

	def test_with_fake_name(self):
		params_ = {'name' : 'Salman Syed'}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)
		self.assertEqual(response.json()['count'], 0)

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