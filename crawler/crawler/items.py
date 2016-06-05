from scrapy_djangoitem import DjangoItem
from main.models import PlayerID

class PlayerIdItem(DjangoItem):
	"""
	Scraped player id is saved in PlayerID model.

	Attributes:
		django_model (object): Django model for saving player id

	"""
	django_model = PlayerID
