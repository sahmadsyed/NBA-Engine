from django.contrib import admin
from app1.models import Player, Statistics


class PlayerAdmin(admin.ModelAdmin):
	search_fields = ['name']
admin.site.register(Player, PlayerAdmin)


class StatsAdmin(admin.ModelAdmin):
	fieldsets = [('Player Statistics', {'fields': ['name', 'season', 'team', 'ppg', 'apg', 'rpg', 'spg', 'bpg', 'fg', 'tfg', 'mpg', 'ft', 'gp', 'gs']})]
	list_filter = ['name']
	search_fields = ['name']
admin.site.register(Statistics, StatsAdmin)