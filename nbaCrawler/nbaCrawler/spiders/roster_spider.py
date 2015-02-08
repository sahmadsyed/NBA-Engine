import scrapy
from nbaCrawler.items import RosterCrawler

class RosterSpider(scrapy.Spider):
	name = 'RosterSpider'
	allow_domains = ['http://en.wikipedia.org/']
	start_urls = ['http://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters']

	def parse(self,response):
		resp = response.xpath('//table[@class = "sortable"]//tr/td[3]/a/@href')
		wiki = 'http://en.wikipedia.org'
		for player in resp:
			roster_item = RosterCrawler()
			roster_item['player_wiki'] = '%s%s' % (wiki, player.extract())
			yield roster_item
			
			
			



