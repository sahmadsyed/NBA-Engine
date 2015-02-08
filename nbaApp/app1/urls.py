from django.conf.urls import patterns, url
from app1 import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^searchresult\=/$', views.no_player_name, name = 'no_player_name'),
                       url(r'^searchresult\=(?P<name>.+)/$', views.player_name, name = 'player_name'),
                       url(r'^advsearch/$', views.adv_search, name = 'adv_search'))
