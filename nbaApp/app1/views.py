from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from app1.models import Player, Statistics

LAST_SEASON = 2013

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
        stats = filter(lambda x: x == player.url, last_season_stats)
        if stats:
            player_info = {'info': player, 'stats': stats[0]}
            player_list.append(player_info)

    template = loader.get_template('app1/index.html')
    context = RequestContext(request,
                             {'player_list': player_list})
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
    

