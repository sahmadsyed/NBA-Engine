from django.template import RequestContext, loader
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from apiclient.discovery import build
from apiclient.errors import HttpError
from app1.models import Player, Statistics, PlayerID
from app1.serializers import StatisticsSerializer, PlayerSerializer
from app1.utils import LogHandler
from app1.forms import EmailForm
from smtplib import SMTP
from logging import ERROR, INFO
from requests import get
from datetime import datetime
from itertools import dropwhile


POS_DICT = {'Guard': 'G', 'Forward': 'F', 'Center': 'C', 'Power forward': 'PF', 'Small forward': 'SF', 'Shooting guard': 'SG', 'Point guard': 'PG'}
LOGGER = LogHandler(__name__)
STATS_URL = 'http://stats.nba.com/stats/playercareerstats'
LEAGUE_ID = '00'
PER_MODE = 'PerGame'
CURRENT_SEASON_STATS_KEY = 'current_season_stats'
NOW = datetime.now()
if NOW.month >= 11:
    CURRENT_SEASON = '%s-%s' % (NOW.year, str(NOW.year + 1)[-2:])
else:
    CURRENT_SEASON = '%s-%s' % (NOW.year - 1, str(NOW.year)[-2:])


class PlayersList(APIView):
    permission_classes = (IsAuthenticated,)

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
            query = query.filter(year_enter_league = draft_year_)
        if position_:
            if position_.lower() not in ['center', 'forward', 'guard']:
                raise NotFound('Incorrect position')
            query = query.filter(position__iexact = position_)
        return query

class PastStatisticsList(APIView):
    permission_classes = (IsAuthenticated,)

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
            season_ = str(season_)
            if not season_.isdigit():
                raise ParseError('Season must be a positive integer')
            if len(season_) != 4:
                raise ParseError('Season must be the following format: yyyy')
            formatted_season = '%s-%s' % (season_, str(int(season_) + 1)[-2:])
            query = query.filter(season = formatted_season)
        return query

def main(request):
    template = loader.get_template('app1/main.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def cache_current_season_stats():
    player_ids = [p.player_id for p in PlayerID.objects.all()]
    params_ = {'LeagueID' : LEAGUE_ID, 'PerMode' : PER_MODE}
    current_season_stats = []
    print 'Caching........'
    for play_id in player_ids:
        try:
            params_['PlayerID'] = play_id
            request = get(STATS_URL, params=params_).json()
            name_ = Player.objects.get(player_id=play_id).name
            stats_list = request['resultSets'][0]['rowSet']
            current_stats = [i for i in dropwhile(lambda s: s[1] != CURRENT_SEASON, stats_list)]

            if current_stats:
                stat = current_stats[-1]
                stats = Statistics()
                stats.name = name_
                stats.ppg = stat[26]
                stats.apg = stat[21]
                stats.rpg = stat[20]
                stats.spg = stat[22]
                stats.bpg = stat[23]
                stats.fg = stat[11]
                stats.tfg = stat[14]
                stats.mpg = stat[8]
                stats.ft = stat[17]
                stats.gp = stat[6]
                stats.to = stat[24]
                stats.team = stat[4]
                stats.season = stat[1]
                stats.player_id = play_id
                current_season_stats.append(stats)
                print('Cached: %s' % name_)
        except Exception, e:
            LOGGER.log(ERROR, 'Caching Error')
            LOGGER.log(ERROR, 'ID: %d' % play_id)
            LOGGER.log(ERROR, 'Error: %s' % e)

    cache.set(CURRENT_SEASON_STATS_KEY, current_season_stats)

def player_name(request, pname):
    if not cache.get(CURRENT_SEASON_STATS_KEY):
        cache_current_season_stats()
    current_season_stats = cache.get(CURRENT_SEASON_STATS_KEY)
    players = Player.objects.filter(name__contains = pname)

    player_list = []
    for player in players:
        recent_stat = filter(lambda s: s.player_id == player.player_id, current_season_stats)
        if recent_stat:
            player_list.append({'info': player, 'stats': recent_stat[0]})
        else:
            LOGGER.log(INFO, 'Missing current season stats: %s' % player.name)
            player_list.append({'info': player, 'stats': []})

    template = loader.get_template('app1/query.html')
    context = RequestContext(request, {'player_list': player_list})
    return HttpResponse(template.render(context))

def no_player_name(request):
    player_list = []
    template = loader.get_template('app1/query.html')
    context = RequestContext(request, {'player_list': player_list})
    return HttpResponse(template.render(context))
    
def player_page(request, pid):
    template = loader.get_template('app1/profile.html')
    player = Player.objects.get(player_id = pid)
    stats = Statistics.objects.filter(player_id = pid)
    if not stats:
        raise Http404
        
    try:
        youtube = build('youtube', 'v3', developerKey = 'AIzaSyC0To03T3OlRJHT03gvErJmeFQ5cbsauLo')
        response = youtube.search().list(part = 'id', 
                                         q = player.name,
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

def api_docs(request):
    template = loader.get_template('app1/apidocs.html');
    context = RequestContext(request);
    return HttpResponse(template.render(context));

def request_token(request):
    form = EmailForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        try:
            user = User.objects.get_by_natural_key(email)
        except ObjectDoesNotExist:
            user = User.objects.create_user(email)

        token = Token.objects.get_or_create(user=user)

        fromaddr = 'pqalmsc@gmail.com'
        toaddr = email
        msg = 'Subject: %s\n\n%s' % ('NBA Authentication Token', 'Authentication Token: %s' % token[0].key)

        username = USERNAME
        password = PASSWORD
        
        server = SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddr, msg)
        server.quit()
        return HttpResponse('Success! Authentication token sent to: %s' % email)
    else:
        return HttpResponse('Error! Invalid email address')