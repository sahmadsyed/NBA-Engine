from rest_framework import serializers
from main.models import Player, Statistics


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ('id', 'name', 'ppg', 'apg', 'rpg', 'spg', 'bpg', 'fg', 'tfg', 'mpg', 'ft', 'gp', 'to', 'team', 'season')

class PlayerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Player
		fields = ('id', 'name', 'number', 'image', 'year_enter_league', 'position', 'height', 'weight', 'current_team')
