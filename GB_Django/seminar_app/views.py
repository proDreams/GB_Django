from random import randint

from django.http import HttpResponse
from django.shortcuts import render

from seminar_app.models import GameModel, Author


def index(request):
    result = ('TAILS', 'HEADS')[randint(0, 1)]

    game = GameModel(result=result)
    game.save()

    return HttpResponse(f'{game}')


def last_games(request):
    last = GameModel().return_last(5)
    last_str = ['<br>' + str(i) for i in last]
    return HttpResponse(last_str)

def autor(request):
    res = Author.objects.all()
    print(res)
    res1 = ''
    for i in res:
        res1 += str(i) + '<br>'
    return HttpResponse(f'{res1}')