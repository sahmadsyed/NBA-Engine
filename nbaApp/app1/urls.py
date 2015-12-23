from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from app1 import views
from rest_framework.authtoken import views as rest_views

urlpatterns = patterns('',
                       url(r'^$', views.main, name='main'),
                       url(r'^search/$', views.no_player_name, name = 'no_player_name'),
                       url(r'^search/(?P<pname>.+)/$', views.player_name, name = 'player_name'),
                       url(r'^api/players/$', views.PlayersList.as_view(), name = 'players_list'),
                       url(r'^api/past_statistics/$', views.PastStatisticsList.as_view(), name = 'past_stats_list'),
                       url(r'^api/current_statistics/$', views.CurrentStatistics.as_view(), name = 'current_stats_list'),
                       url(r'^api/auth_token/$', rest_views.obtain_auth_token, name = 'auth_token'),
                       url(r'^api/$', views.api_docs, name = 'api_docs'),
                       url(r'^api/request_email_confirm/$', views.request_token, name = 'request_token'),
                       url(r'^contact/$', views.contact_us_page, name = 'contact_us_page'),
                       url(r'^contact_email_confirm/$', views.contact_us, name = 'contact_us_email_confirm'),
                       url(r'^profile/(?P<pid>.+)/$', views.player_page, name = 'player_page'))
					   
urlpatterns = format_suffix_patterns(urlpatterns)