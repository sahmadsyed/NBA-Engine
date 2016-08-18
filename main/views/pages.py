from logging import ERROR, INFO
from itertools import dropwhile

from django.template import RequestContext, loader
from django.http import Http404, HttpResponse
from django.core.cache import cache
from django.core.paginator import Paginator, InvalidPage
from apiclient.discovery import build
from apiclient.errors import HttpError

from utils import LogHandler, get_current_season
from main.views.helpers.current_season_stats_job import CurrentSeasonStatsJob
from main.models import Player, Statistics, PlayerID
from main.serializers import StatisticsSerializer, PlayerSerializer


# constants
LOGGER = LogHandler(__name__)
SEARCH_PLAYER_KEY = 'searched'


def home(request):
    """Renders home page."""

    template = loader.get_template('main/home.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def search_results(request, pname):
    """
    Renders player results based on search query.

    Args:
        pname (str): Player name search query

    """
    searched_players = cache.get(SEARCH_PLAYER_KEY)
    if searched_players and pname in searched_players:
        player_list = searched_players[pname]
    else:
        current_season_stats = CurrentSeasonStatsJob().get()
        players = Player.objects.filter(name__contains = pname)

        player_list = []
        for player in players:
            recent_stat = filter(lambda s: s.player_id == player.player_id, current_season_stats)
            if recent_stat:
                player_list.append({'info': player, 'stats': recent_stat[0]})
            else:
                LOGGER.log(INFO, 'Missing current season stats: %s' % player.name)
                player_list.append({'info': player, 'stats': []})

        cache.set(SEARCH_PLAYER_KEY, {pname : player_list}, 600)

    paginator = Paginator(player_list, 15)
    page = request.GET.get('page')
    try:
        player_list = paginator.page(page)
        current_page = int(page)
    except InvalidPage:
        player_list = paginator.page(1)
        current_page = 1

    if paginator.num_pages > 1:
        page_range = paginator.page_range
    else:
        page_range = False

    template = loader.get_template('main/query.html')
    context = RequestContext(request, {'player_list': player_list, 'page_range': page_range, 'current_page': current_page, 'search_query': pname})
    return HttpResponse(template.render(context))

def no_player_name(request):
    """Renders page for no results found."""

    player_list = []
    template = loader.get_template('main/query.html')
    context = RequestContext(request, {'player_list': player_list})
    return HttpResponse(template.render(context))

def player_profile(request, pid):
    """
    Renders player page.

    Args:
        pid (integer): id of player

    """
    template = loader.get_template('main/profile.html')
    player = Player.objects.get(player_id = pid)
    stats = Statistics.objects.filter(player_id = pid)
    if not stats:
        raise Http404

    try:
        youtube = build('youtube', 'v3', developerKey = settings.YOUTUBE_DEVELOPER_KEY)
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
        LOGGER.log(ERROR, 'YouTube API Call Error: %s' % e)
        raise e

    context = RequestContext(request, {'player': player, 'videos': videos, 'stats': stats})
    return HttpResponse(template.render(context))

def api_docs(request):
    """Renders API docs page."""

    template = loader.get_template('main/api-docs.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def contact_us(request):
    """Renders 'Contact Us' page."""

    template = loader.get_template('main/contact-us.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
