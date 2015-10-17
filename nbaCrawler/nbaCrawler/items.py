import scrapy
from scrapy_djangoitem import DjangoItem
from app1.models import Player, Statistics, PlayerID


class StatsCrawler(DjangoItem):
	django_model = Statistics

class InfoCrawler(DjangoItem):
	django_model = Player

class RosterCrawler(DjangoItem):
	django_model = PlayerID
