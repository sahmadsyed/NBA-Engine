from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^player_list/', include('app1.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
