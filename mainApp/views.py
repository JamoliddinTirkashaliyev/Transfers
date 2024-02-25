from django.shortcuts import render

from mainApp.models import *
from datetime import date


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


def clubs_players(request, nom):
    context = {
        'players': Player.objects.filter(club=Club.objects.filter(nom=nom).first())
    }
    return render(request, 'clubs-players.html', context)


def stats(request):
    return render(request, 'stats.html')


def about(request):
    return render(request, 'about.html')


def u_20(request):
    hozirgi_sana = str(date.today())
    yil = int(hozirgi_sana[:4]) - 20
    yangi_sana = hozirgi_sana.replace(hozirgi_sana[:4], str(yil))
    players = Player.objects.filter(t_yil__gt=yangi_sana)
    context = {
        'players': players
    }
    return render(request, 'U-20 players.html', context=context)


def tryouts(request):
    return render(request, 'tryouts.html')


def transfer_archive(request):
    return render(request, 'transfer-archive.html')


def season2017_18(request):
    context = {
        'transfers': Transfer.objects.filter(mavsum='2017/2018')

    }
    return render(request, '2017-18season.html', context)


def season2018_19(request):
    context = {
        'transfers': Transfer.objects.filter(mavsum='2018/2019')

    }
    return render(request, '2017-18season.html', context)


def season2019_20(request):
    context = {
        'transfers': Transfer.objects.filter(mavsum='2019/2020')

    }
    return render(request, '2017-18season.html', context)


def season2020_21(request):
    context = {
        'transfers': Transfer.objects.filter(mavsum='2020/2021')

    }
    return render(request, '2017-18season.html', context)
