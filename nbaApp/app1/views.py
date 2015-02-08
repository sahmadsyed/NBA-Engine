from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from app1.models import *
def index(request):
    player_list = Player.objects.all()
    template = loader.get_template('app1/index.html')
    context = RequestContext(request,
                             {'player_list':player_list})
    return HttpResponse(template.render(context))
def player_name(request,name):
    player_list_orig = Player.objects.all()
    player_list = []
    enter_val_len = len(name)
    if len(name) == 1:
        mod_name = name.upper()
    else:
        mod_name = name[0].upper() + name[1:].lower()
    for player in player_list_orig:
        if ((player.first_name[0:enter_val_len] == mod_name) or
            (player.last_name[0:enter_val_len] == mod_name)):
            player_list.append(player)

    template = loader.get_template('app1/index.html')
    context = RequestContext(request,
                             {'player_list':player_list})
    return HttpResponse(template.render(context))

def no_player_name(request):
    player_list = []
    template = loader.get_template('app1/index.html')
    context = RequestContext(request,
                             {'player_list':player_list})
    return HttpResponse(template.render(context))

def adv_search(request):
    template = loader.get_template('app1/index2.html');
    context = RequestContext(request);
    return HttpResponse(template.render(context));
    

