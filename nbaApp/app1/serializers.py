from rest_framework import serializers
from app1.models import Player, Statistics


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ('id', 'name', 'ppg', 'apg', 'rpg', 'spg', 'bpg', 'fg', 'tfg', 'mpg', 'ft', 'gp', 'gs', 'team', 'season')

class PlayerSerializer(serializers.ModelSerializer):
	height = serializers.IntegerField(source = 'height_inches')
	weight = serializers.IntegerField(source = 'weight_lb')
	class Meta:
		model = Player
		fields = ('id', 'name', 'image', 'draft_year', 'position', 'height', 'weight')