TEAMS_DICT = {'Boston': 'Celtics',
			  'Brooklyn': 'Nets',
			  'New York': 'Knicks',
			  'Philadelphia': '76ers',
			  'Toronto': 'Raptors',
			  'Chicago': 'Bulls',
			  'Cleveland': 'Cavaliers',
			  'Detroit': 'Pistons',
			  'Indiana': 'Pacers',
			  'Milwaukee': 'Bucks',
			  'Atlanta': 'Hawks',
			  'Charlotte': 'Hornets',
			  'Miami': 'Heat',
			  'Orlando': 'Magic',
			  'Washington': 'Wizards',
			  'Dallas': 'Mavericks',
			  'Houston': 'Rockets',
			  'Memphis': 'Grizzlies',
			  'New Orleans': 'Pelicans',
			  'San Antonio': 'Spurs',
			  'Denver': 'Nuggets',
			  'Minnesota': 'Timberwolves',
			  'Oklahoma City': 'Thunder',
			  'Portland': 'Trail Blazers',
			  'Utah': 'Jazz',
			  'Golden State': 'Warriors',
			  'Phoenix': 'Suns',
			  'Sacramento': 'Kings'}

for stat in Statistics.objects.all():
	if TEAMS_DICT.get(stat.team):
		stat.team = "%s %s" % (stat.team ,TEAMS_DICT.get(stat.team))
		stat.save()