from django.contrib import admin
from main.models import Player, Statistics, PlayerID


class PlayerAdmin(admin.ModelAdmin):
	"""
	Customizes admin page for saved Player objects.

	Attributes:
		search_fields (List[str]): fields of Player model to search with

	"""

	search_fields = ['name']

admin.site.register(Player, PlayerAdmin)


class StatsAdmin(admin.ModelAdmin):
	"""
	Customizes admin page for saved Statistics objects.

	Attributes:
		search_fields (List[str]): fields of Statistics model to search with
		list_filter (List[str]): fields of Statistics model to filter with

	"""

	list_filter = ['name']
	search_fields = ['name']

admin.site.register(Statistics, StatsAdmin)


class PlayerIdAdmin(admin.ModelAdmin):
	"""
	Customizes admin page for saved PlayerID objects.

	Attributes:
		search_fields (List[str]): fields of PlayerID model to search with

	"""

	search_fields = ['player_id']

admin.site.register(PlayerID, PlayerIdAdmin)
