import scrapy
from logging import ERROR, INFO
from itertools import count
from xml.dom.minidom import parse
from nbaCrawler.items import RosterCrawler
from nbaCrawler.log_handler import LogHandler


class RosterSpider(scrapy.Spider):
	name = 'RosterSpider'
	allow_domains = ['http://nba.com/']
	logger = LogHandler(__name__)
	xml_dom = parse('/home/salman/NBA-Players-Database-Website/nbaCrawler/nbaCrawler/current_players.xml')
	current_players = xml_dom.getElementsByTagName('loc')
	start_urls = [p.childNodes[0].data for p in current_players]

	def parse(self, response):
		try:
			resp = response.xpath('//a[@id="tab-stats"]/@href')
			for i in count(0, 2):
				try:
					player = resp[i]
				except IndexError:
					break
				roster_item = RosterCrawler()
				url_ = player.extract()
				self.logger.log(INFO, 'Player URL: %s' % url_)
				first = url_.index('!') + 2
				last = len(url_) - 1
				id_ = url_[first:last]
				roster_item['player_id'] = id_
				self.logger.log(INFO, 'Player ID scraped: %s' % id_)
				yield roster_item				
		except Exception, e:
			self.logger.log(ERROR, '%s - %s (URL: %s)' % ('Roster extraction error', str(e), response.url))
			return