import requests
from unittest import skip

from main.tests.test_past_statistics_endpoint import PastStatisticsEndpointTests


class CurrentStatisticsEndpointTests(PastStatisticsEndpointTests):
	URL = 'http://127.0.0.1:8000/api/current_statistics/'

	def test_with_no_params(self):
		response = requests.get(self.URL, headers = self.VALID_HEADER)
		self.assertEqual(response.status_code, requests.codes.ok)

	@skip('no season param for current season')
	def test_with_name_and_season(self):
		pass

	@skip('no season param for current season')
	def test_with_alpha_season(self):
		pass

	@skip('no season param for current season')
	def test_with_ancient_season(self):
		pass
