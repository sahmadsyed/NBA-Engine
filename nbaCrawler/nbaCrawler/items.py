import scrapy
from scrapy_djangoitem import DjangoItem
from app1.models import Player, Statistics


class StatsCrawler(DjangoItem):
	django_model = Statistics

class InfoCrawler(DjangoItem):
	django_model = Player

class RosterCrawler(scrapy.Item):
	player_wiki = scrapy.Field()

