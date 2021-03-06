from logging import ERROR, INFO
from itertools import count
from xml.dom.minidom import parse
from urllib2 import urlopen

import scrapy

from crawler.items import PlayerIdItem
from utils import LogHandler


#constants
CURRENT_PLAYERS_SITEMAP = 'http://www.nba.com/current_players.xml'
LOGGER = LogHandler(__name__)

class PlayerIdSpider(scrapy.Spider):
	"""
	Scrapes current NBA players' ids from their nba.com page.

	Attributes:
		name (str): Name of spider
		allow_domains (List[str]): Domains which spider is allowed to scrape
		current_players (List[str]): Nba.com urls of current NBA players
		start_urls (List[str]): Urls which spider will scrape
	"""

	name = 'PlayerIdSpider'
	allow_domains = ['http://nba.com/']
	current_players = parse(urlopen(CURRENT_PLAYERS_SITEMAP)).getElementsByTagName('loc')
	start_urls = [p.childNodes[0].data for p in current_players]

	def parse(self, response):
		"""
		Acquires NBA player id from the DOM of their page.

		Args:
			response (object): Scraped response object

		Yields:
			PlayerIdItem instance with scraped id if successful, None otherwise

		"""
		try:
			resp = response.xpath('//a[@id="tab-stats"]/@href')
			for i in count(0, 2):
				try:
					player = resp[i]
				except IndexError:
					break
				player_id_item = PlayerIdItem()
				url_ = player.extract()
				LOGGER.log(INFO, 'Player URL: %s' % url_)
				first = url_.index('!') + 2
				last = len(url_) - 1
				id_ = url_[first:last]
				player_id_item['player_id'] = id_
				LOGGER.log(INFO, 'Player ID scraped: %s' % id_)
				yield player_id_item
		except Exception, e:
			LOGGER.log(ERROR, '%s - %s (URL: %s)' % ('Player id extraction error', str(e), response.url))
