from django.contrib import admin

# Register your models here.
from app1.models import *

#admin.site.register(Statistics)
admin.site.register(Player)


class StatsAdmin(admin.ModelAdmin):
	fieldsets = [('Player Statistics',{'fields': ['first_name', 'last_name', 'season', 'team', 'ppg', 'apg', 'rpg', 'spg', 'bpg', 'fg', 'tfg', 'mpg', 'ft', 'gp', 'gs']})]
	list_filter = ['first_name', 'last_name']
	search_fields = ['first_name', 'last_name']
admin.site.register(Statistics, StatsAdmin)