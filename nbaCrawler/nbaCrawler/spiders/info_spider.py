import scrapy
from logging import ERROR, WARNING, DEBUG
from json import loads
from nbaCrawler.items import InfoCrawler
from nbaCrawler.log_handler import LogHandler

class InfoSpider(scrapy.Spider):
	name = 'InfoSpider'
	allow_domains = ['http://en.wikipedia.org/']
	current_players = loads(open('playerswiki.json').read())
	start_urls = [player['player_wiki'] for player in current_players]
	logger = LogHandler(__name__)

	def parse(self, response):
		try:
			info_item = InfoCrawler()
			info_item['url'] = response.url
			player_name = response.xpath('//title/text()').extract()[0]
			player_name = player_name[:player_name.find(' - Wikipedia, the free encyclopedia')]
			if '(' in player_name:
				player_name = player_name[:player_name.find('(') - 1]
			info_item['name'] = unicode(player_name)

			info_crude = response.xpath('//table[@class = "infobox vcard"][1]//th/text()|//table[@class = "infobox vcard"][1]//td/text()|//table[@class = "infobox vcard"][1]//th/text()|//table[@class = "infobox vcard"][1]//td/text()|//table[@class = "infobox vcard"][1]//th/a/text()|//table[@class = "infobox vcard"][1]//td/a/text()')
			info = [i.extract() for i in info_crude]
			height_index = info.index('Listed height') + 1
			height_str = str(info[height_index].replace(u'\xa0', u' '))
			info_item['height'] = height_str
			feet = int(height_str[0 : height_str.index(' ')])
			inches = int(height_str[height_str.index('t') + 2 : height_str.index('i') - 1])
			info_item['height_inches'] = feet*12 + inches
			weight_index = info.index('Listed weight') + 1
			weight_str = str(info[weight_index].replace(u'\xa0', u' '))
			info_item['weight'] = weight_str
			pounds = int(weight_str[0 : weight_str.index(' ')])
			info_item['weight_lb'] = pounds
			positions = ['guard', 'forward', 'center', 'power forward', 'small forward', 'shooting guard', 'point guard']
			position = filter(lambda x: x.lower() in positions, info)[0]
			info_item['position'] = position[0].upper() + position[1:].lower()
			try:
				img_src = response.xpath('//table[@class = "infobox vcard"][1]//img[1]/@src')
				info_item['image'] = str(img_src.extract()[0])
			except Exception, e:
				self.logger.log(WARNING, '%s (URL: %s)' % ('Missing image', response.url))
			try:
				draft_year_index = info.index('NBA draft') + 1
				info_item['draft_year'] = info[draft_year_index]
			except Exception, e:
				self.logger.log(WARNING, '%s (URL: %s)' % ('Missing draft year', response.url))
			return info_item
		except Exception, e:
			self.logger.log(ERROR, '%s - %s (URL: %s)' % ('Player info extraction error', str(e), response.url))