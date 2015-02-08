from django.contrib import admin
from app1.models import Player, Statistics

admin.site.register(Player)


class StatsAdmin(admin.ModelAdmin):
	fieldsets = [('Player Statistics',{'fields': ['first_name', 'last_name', 'season', 'team', 'ppg', 'apg', 'rpg', 'spg', 'bpg', 'fg', 'tfg', 'mpg', 'ft', 'gp', 'gs']})]
	list_filter = ['name']
	search_fields = ['name']
admin.site.register(Statistics, StatsAdmin)