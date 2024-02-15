from django.shortcuts import render

from mainApp.models import *


def index(request):
    return render(request, 'index.html')


def clubs(request):
    context = {
        'clubs': Club.objects.all()
    }
    return render(request, 'clubs.html', context)


def players(request):
    context = {
        'players': Player.objects.all()
    }
    return render(request, 'players.html', context)


def country_clubs(request, country_name):
    context = {
        'clubs': Club.objects.filter(davlat__nom__contains=country_name)
    }
    return render(request, 'country-clubs.html', context)


