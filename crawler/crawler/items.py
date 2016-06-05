from scrapy_djangoitem import DjangoItem
from main.models import PlayerID

class PlayerIdItem(DjangoItem):
	django_model = PlayerID
