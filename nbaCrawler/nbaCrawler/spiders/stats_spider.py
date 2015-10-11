import scrapy
from logging import ERROR, WARNING, DEBUG
from json import loads
from nbaCrawler.items import StatsCrawler
from nbaCrawler.log_handler import LogHandler

class StatsSpider(scrapy.Spider):
	name = 'StatsSpider'
	allow_domains = ['http://en.wikipedia.org/']
	current_players = loads(open("playerswiki.json").read())
	start_urls = [player['player_wiki'] for player in current_players]
	logger = LogHandler(__name__)

	def _safe_insert(self, stats_item, resp, key, count, index):
		if resp[count[0] + index].extract() == u'\u2020':
			count[0]+= 1
		stats_item[key] = resp[count[0] + index].extract()

	def parse(self, response):
		player_name = response.xpath('//title/text()').extract()[0]
		player_name = player_name[:player_name.find(' - Wikipedia, the free encyclopedia')]
		if '(' in player_name:
			player_name = player_name[:player_name.find('(') - 1]
		resp = response.xpath('//span[@id = "Regular_season"]/text()|//span[@id = "NBA_regular_season"]/text()|//table[@class = "wikitable sortable"]//td/a/text()|//table[@class = "wikitable sortable"]//td/text()|//table[@class = "wikitable sortable"]//td/b/text()|//dt/text()')
		reg_index = -1
		for i in resp:
			try:
				if i.extract() == 'Regular season' or i.extract() == 'NBA regular season':
					reg_index = resp.index(i)
					break
			except Exception, e:
				self.logger.log(WARNING, '%s - %s (URL: %s)' % ('Stats location error', str(e), response.url))
				continue
		if reg_index == -1:
			self.logger.log(WARNING, '%s (URL: %s)' % ('No stats', response.url))
			return
		resp = resp[reg_index + 1:]
		stats_end = False
		count = [0]
		while not stats_end:
			try:
				stats_item = StatsCrawler()
				stats_item['name'] = unicode(player_name)
				stats_item['url'] = response.url
				if resp[count[0]].extract() == 'Career':
					stats_item['season'] = 'Career'
					stats_item['team'] = 'Career'
					stats_end = True
					count[0]-= 1
				else:
					self._safe_insert(stats_item, resp, 'season', count, 0)
					stats_item['season'] = resp[count[0]].extract()[0:4]
					self._safe_insert(stats_item, resp, 'team', count, 1)
				self._safe_insert(stats_item, resp, 'gp', count, 2)
				self._safe_insert(stats_item, resp, 'gs', count, 3)
				self._safe_insert(stats_item, resp, 'mpg', count, 4)
				self._safe_insert(stats_item, resp, 'fg', count, 5)
				self._safe_insert(stats_item, resp, 'tfg', count, 6)
				self._safe_insert(stats_item, resp, 'ft', count, 7)
				self._safe_insert(stats_item, resp, 'rpg', count, 8)
				self._safe_insert(stats_item, resp, 'apg', count, 9)
				self._safe_insert(stats_item, resp, 'spg', count, 10)
				self._safe_insert(stats_item, resp, 'bpg', count, 11)
				self._safe_insert(stats_item, resp, 'ppg', count, 12)
				count[0]+=13
				yield stats_item
			except Exception, e:
				self.logger.log(ERROR, '%s - %s (URL: %s)' % ('Stats extraction error', str(e), response.url))
				return