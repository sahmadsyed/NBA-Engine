from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse
from django.core.exceptions import MultipleObjectsReturned
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from app1.models import Player, Statistics
from app1.serializers import StatisticsSerializer, PlayerSerializer
from log_handler import LogHandler
from itertools import dropwhile
from logging import DEBUG


LAST_SEASON = 2013
POS_DICT = {'Guard': 'G', 'Forward': 'F', 'Center': 'C', 'Power forward': 'PF', 'Small forward': 'SF', 'Shooting guard': 'SG', 'Point guard': 'PG'}
LOGGER = LogHandler('views')

class PlayersList(generics.ListAPIView):
    serializer_class = PlayerSerializer
    def get_queryset(self):
        query = Player.objects.all()
        name_ = self.request.query_params.get('name')
        draft_year_ = self.request.query_params.get('draft_year')
        position_ = self.request.query_params.get('position')
        height_ = self.request.query_params.get('height')
        weight_ = self.request.query_params.get('weight')
        if name_:
            query = query.filter(name = name_)
        if draft_year_:
            query = query.filter(draft_year = draft_year_)
        if position_:
            query = query.filter(position = position_)
        if height_:
            query = query.filter(height = height_)
        if weight_:
            query = query.filter(weight = weight_)
        return query

class StatisticsList(generics.ListAPIView):
    serializer_class = StatisticsSerializer
    def get_queryset(self):
        name_ = self.request.query_params.get('name')
        query = Statistics.objects.filter(name = name_)
        return query

def main(request):
    player_list = []
    template = loader.get_template('app1/main.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def player_name(request, pname):
    players = Player.objects.filter(name__contains = pname)
    last_season_stats = Statistics.objects.filter(name__contains = pname, season = LAST_SEASON)
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
    template = loader.get_template('app1/query.html')
    context = RequestContext(request, {'player_list': player_list})
    return HttpResponse(template.render(context))

def no_player_name(request):
    player_list = []
    template = loader.get_template('app1/query.html')
    context = RequestContext(request, {'player_list': player_list})
    return HttpResponse(template.render(context))

def adv_search(request):
    template = loader.get_template('app1/main.html');
    context = RequestContext(request);
    return HttpResponse(template.render(context));
    
def player_page(request, pname):
    template = loader.get_template('app1/profile.html')
    player_name = pname.replace('_', ' ')
    find = Player.objects.filter(name = player_name)
    if not find:
        raise Http404
    elif len(find) == 1:
        player = find[0]
    else:
        raise MultipleObjectsReturned
    stats = Statistics.objects.filter(url = player.url)
    if not stats:
        raise Http404
        
    try:
        youtube = build('youtube', 'v3', developerKey = 'AIzaSyC0To03T3OlRJHT03gvErJmeFQ5cbsauLo')
        response = youtube.search().list(part = 'id', 
                                         q = player_name,
                                         maxResults = 10,
                                         order = 'date',
                                         safeSearch = 'strict',
                                         type = 'video',
                                         videoDefinition = 'high',
                                         videoDuration = 'short',
                                         videoEmbeddable = 'true').execute()
        video_links = []
        for i in response['items']:
            if 'id' in i and 'videoId' in i['id']:
                video_links.append(str('https://www.youtube.com/v/%s' % i['id']['videoId']))
        videos = video_links
    except HttpError, e:
        raise e
    context = RequestContext(request, {'player': player, 'videos': videos, 'stats': stats})
    return HttpResponse(template.render(context))

