from django.http import HttpResponse
from .models import Game

def funhello(request):
    return HttpResponse("hey");

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

