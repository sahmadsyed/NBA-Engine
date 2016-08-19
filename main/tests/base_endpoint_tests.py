import requests

from rest_framework.test import APITestCase
from django.conf import settings

class BaseEndpointTests(APITestCase):
	URL = None
	VALID_TOKEN = 'Token %s' % settings.TEST_AUTHENTICATION_TOKEN
	VALID_HEADER = {'Authorization' : VALID_TOKEN}
	INVALID_HEADER = {'Authorization' : 'Token invalid'}

	def test_with_no_auth(self):
		response = requests.get(self.URL)
		self.assertEqual(response.status_code, requests.codes.unauthorized)

	def test_with_invalid_auth(self):
		response = requests.get(self.URL, headers = self.INVALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.unauthorized)

	def test_case_insenstive_search(self):
		params_ = {'name' : 'Chris Bosh'}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		r_proper_case = response.json()
		params_['name'] = 'CHRIS BOSH'
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		r_upper_case = response.json()
		params_['name'] = 'chris bosh'
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		r_lower_case = response.json()
		params_['name'] = 'cHRis BOsh'
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		r_mixed_case = response.json()
		self.assertTrue(r_proper_case == r_upper_case == r_lower_case == r_mixed_case)

	def test_with_fake_name(self):
		params_ = {'name' : 'Salman Syed'}
		response = requests.get(self.URL, params = params_, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)
		self.assertEqual(response.json()['count'], 0)
