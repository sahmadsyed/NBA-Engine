from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from app1.models import Player, Statistics
from itertools import dropwhile

LAST_SEASON = 2013
POS_DICT = {'Guard': 'G', 'Forward': 'F', 'Center': 'C', 'Power forward': 'PF', 'Small forward': 'SF', 'Shooting guard': 'SG', 'Point guard': 'PG'}
def index(request):
    player_list = []
    template = loader.get_template('app1/index.html')
    context = RequestContext(request,
                             {'player_list': player_list})
    return HttpResponse(template.render(context))
def player_name(request, name):
    players = Player.objects.filter(name__contains = name)
    last_season_stats = Statistics.objects.filter(name__contains = name, season = LAST_SEASON)
    player_list = []
    for player in players:
        recent_stat = False
        for stat in dropwhile(lambda stat: stat.url != player.url, last_season_stats):
            recent_stat = stat
            break
        if recent_stat:
            player.position = POS_DICT[player.position]
            player_info = {'info': player, 'stats': recent_stat}
            player_list.append(player_info)

    template = loader.get_template('app1/index.html')
    context = RequestContext(request, {'player_list': player_list})
    return HttpResponse(template.render(context))

def no_player_name(request):
    player_list = []
    template = loader.get_template('app1/index.html')
    context = RequestContext(request,
                             {'player_list': player_list})
    return HttpResponse(template.render(context))

def adv_search(request):
    template = loader.get_template('app1/index2.html');
    context = RequestContext(request);
    return HttpResponse(template.render(context));
    

