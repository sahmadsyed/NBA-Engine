from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from app1.models import Player, Statistics
from app1.serializers import StatisticsSerializer, PlayerSerializer
from app1.utils import LogHandler
from app1.forms import EmailForm
from itertools import dropwhile
from logging import DEBUG as d
from smtplib import SMTP


LAST_SEASON = 2013
POS_DICT = {'Guard': 'G', 'Forward': 'F', 'Center': 'C', 'Power forward': 'PF', 'Small forward': 'SF', 'Shooting guard': 'SG', 'Point guard': 'PG'}
LOGGER = LogHandler(__name__)

class PlayersList(APIView):

    def get(self, request, *args, **kwargs):
        query_set = self.get_players()
        serializer = PlayerSerializer(query_set, many=True)
        resp_data = {'count' : len(query_set), 'players' : serializer.data}
        return Response(resp_data)

    def get_players(self):
        query = Player.objects.all()
        name_ = self.request.query_params.get('name')
        draft_year_ = self.request.query_params.get('draft_year')
        position_ = self.request.query_params.get('position')
        if name_:
            query = query.filter(name__iexact = name_)
        if draft_year_:
            if not draft_year_.isdigit():
                raise ParseError('Draft year must be a positive integer')
            query = query.filter(draft_year = draft_year_)
        if position_:
            correct_position = position_.lower() in [pos.lower() for pos in POS_DICT.iterkeys()]
            if not correct_position:
                raise NotFound('Incorrect position')
            query = query.filter(Q(position = position_) | Q(position__endswith = position_))
        return query

class StatisticsList(APIView):
    def get(self, request, *args, **kwargs):
        query_set = self.get_stats()
        serializer = StatisticsSerializer(query_set, many=True)
        resp_data = {'count' : len(query_set), 'stats' : serializer.data}
        return Response(resp_data)

    def get_stats(self):
        name_ = self.request.query_params.get('name')
        if not name_:
            raise ParseError('Missing \'name\'')
        season_ = self.request.query_params.get('season')
        query = Statistics.objects.filter(name__iexact = name_)
        if season_:
            if not season_.isdigit():
                raise ParseError('Season must be a positive integer')
            query = query.filter(season = season_)
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
    template = loader.get_template('app1/apidocs.html');
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

def request_token(request):
    form = EmailForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        user = None
        try:
            user = User.objects.get_by_natural_key(email)
        except ObjectDoesNotExist:
            user = User.objects.create_user(email)

        token = Token.objects.get_or_create(user=user)

        fromaddr = 'salmanahmadsyed@gmail.com'
        toaddrs = email
        msg = 'Authentication Token: %s' % token[0].key

        username = USERNAME
        password = PASSWORD

        server = SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        return HttpResponse('Success! Authentication token sent to: %s' % email)
    else:
        return HttpResponse('Error! Invalid email address')

