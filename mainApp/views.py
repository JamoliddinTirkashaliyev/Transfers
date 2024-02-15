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
def lastest_transfers(request):
    context = {
        'transfers': Transfer.objects.order_by('-sana')

    }
    return render(request, 'latest-transfers.html', context)

def transfer_records(request):
    context = {
        'transfers': Transfer.objects.filter(narx__gt=50)
    }
    return render(request, 'transfer-records.html', context)

def clubs(request):
    context = {
        "clubs": Club.objects.all()
    }
    return render(request, 'clubs.html', context)

