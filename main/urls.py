from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_views

from main.views import api, form_handlers, pages


urlpatterns = patterns('',

                    # page routes
                    url(r'^$', pages.home, name = 'home'),
                    url(r'^search/$', pages.no_player_name, name = 'no_player_name'),
                    url(r'^search/(?P<pname>.+)/$', pages.search_results, name = 'search_results'),
                    url(r'^api/$', pages.api_docs, name = 'api_docs'),
                    url(r'^contact/$', pages.contact_us, name = 'contact_us_page'),
                    url(r'^profile/(?P<pid>.+)/$', pages.player_profile, name = 'player_page'),

                    # api routes
                    url(r'^api/players/$', api.PlayersList.as_view(), name = 'players_list'),
                    url(r'^api/past_statistics/$', api.PastStatisticsList.as_view(), name = 'past_stats_list'),
                    url(r'^api/current_statistics/$', api.CurrentStatistics.as_view(), name = 'current_stats_list'),
                    url(r'^api/auth_token/$', rest_views.obtain_auth_token, name = 'auth_token'),

                    # form handling routes
                    url(r'^api/request_email_confirm/$', form_handlers.request_token, name = 'request_token'),
                    url(r'^contact_email_confirm/$', form_handlers.contact_us, name = 'contact_us_email_confirm'))

urlpatterns = format_suffix_patterns(urlpatterns)
