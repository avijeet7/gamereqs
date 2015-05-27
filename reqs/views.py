from django.http import HttpResponse
from django.shortcuts import render
from .models import Game
from django.contrib.auth.decorators import login_required

def funhello(request):
    return HttpResponse("hey");

@login_required(login_url='/accounts/login/')
def names(request):
    games = Game.objects.all()
    response = ""
    for game in games:
        response += "<a href = /reqs/details/"+str(game.id)+">"
        response += game.name + "</a>\n <br />"
    return HttpResponse(response)

def details(request, id):
    game = Game.objects.get(id=id)
    return HttpResponse(game.reqs)

def add(request, name, reqs):
    temp = Game(name=name, reqs=reqs)
    temp.save()
    return HttpResponse("Inserted.")

