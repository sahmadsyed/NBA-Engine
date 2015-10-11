from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from app1 import views
from rest_framework.authtoken import views as rest_views

urlpatterns = patterns('',
                       url(r'^$', views.main, name='main'),
                       url(r'^searchresult\=/$', views.no_player_name, name = 'no_player_name'),
                       url(r'^searchresult\=(?P<pname>.+)/$', views.player_name, name = 'player_name'),
                       url(r'^advsearch/$', views.adv_search, name = 'adv_search'),
                       url(r'^api/players/$', views.PlayersList.as_view(), name = 'players_list'),
                       url(r'^api/statistics/$', views.StatisticsList.as_view(), name = 'stats_list'),
                       url(r'^api/auth_token/$', rest_views.obtain_auth_token, name = 'auth_token'),
                       url(r'^api/email_confirm/$', views.request_token, name = 'request_token'),
                       url(r'^(?P<pname>.+)/$', views.player_page, name = 'player_page'))
					   
urlpatterns = format_suffix_patterns(urlpatterns)