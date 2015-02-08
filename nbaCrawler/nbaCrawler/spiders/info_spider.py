import scrapy, json
from nbaCrawler.items import InfoCrawler
from nbaCrawler.errorutils import write_error

class InfoSpider(scrapy.Spider):
	name = 'InfoSpider'
	allow_domains = ['http://en.wikipedia.org/']
	current_players = json.loads(open("playerswiki2.json").read())
	start_urls = [player['player_wiki'] for player in current_players]
	
	def parse(self, response):
		try:
			info_item = InfoCrawler()
			player_name = response.xpath('//title/text()').extract()[0]
			player_name = player_name[:player_name.find(' - Wikipedia, the free encyclopedia')]
			if '(' in player_name:
				player_name = player_name[:player_name.find('(') - 1]
			info_item['name'] = unicode(player_name)

			# last_space = player_name.rfind(' ')
			# if last_space == -1:
			# 	last_space = len(player_name)
			# first_name = player_name[0:last_space]
			# last_name = player_name[last_space + 1:]
			# info_item['first_name'] = unicode(first_name)
			# info_item['last_name'] = unicode(last_name)

			try:
				img_src = response.xpath('//table[@class = "infobox vcard"][1]//img[1]/@src')
				info_item['image'] = str(img_src.extract()[0])
			except Exception as e:
				write_error('minorerrors.txt', str(e), str(response.url), 'Missing image')

			info_crude = response.xpath('//table[@class = "infobox vcard"][1]//th/text()|//table[@class = "infobox vcard"][1]//td/text()|//table[@class = "infobox vcard"][1]//th/text()|//table[@class = "infobox vcard"][1]//td/text()|//table[@class = "infobox vcard"][1]//th/a/text()|//table[@class = "infobox vcard"][1]//td/a/text()')
			info = [i.extract() for i in info_crude]
			height_index = info.index('Listed height') + 1
			info_item['height'] = info[height_index]
			weight_index = info.index('Listed weight') + 1
			info_item['weight'] = info[weight_index]

			try:
				draft_year_index = info.index('NBA draft') + 1
				info_item['draft_year'] = info[draft_year_index]
			except Exception as e:
				write_error('minorerrors.txt', str(e), str(response.url), 'Missing draft year')

			positions = ['Guard', 'Forward', 'Center', 'Power forward', 'Small forward', 'Shooting guard', 'Point guard']
			position = list(set(positions) & set(info))[0]
			info_item['position'] = position		
			return info_item
		except Exception as e:
			write_error('majorerrors.txt', str(e), str(response.url))


		
			
			



