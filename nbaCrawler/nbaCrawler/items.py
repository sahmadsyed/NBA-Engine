from scrapy_djangoitem import DjangoItem
from app1.models import PlayerID

class RosterCrawler(DjangoItem):
	django_model = PlayerID
