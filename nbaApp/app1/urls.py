from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from app1 import views

urlpatterns = patterns('',
                       url(r'^$', views.main, name='main'),
                       url(r'^searchresult\=/$', views.no_player_name, name = 'no_player_name'),
                       url(r'^searchresult\=(?P<pname>.+)/$', views.player_name, name = 'player_name'),
                       url(r'^(?P<pname>.+)/$', views.player_page, name = 'player_page'),
                       url(r'^advsearch/$', views.adv_search, name = 'adv_search'),
                       url(r'^api/players$', views.PlayersList.as_view(), name = 'players_list'),
                       url(r'^api/statistics$', views.StatisticsList.as_view(), name = 'stats_list'))

urlpatterns = format_suffix_patterns(urlpatterns)