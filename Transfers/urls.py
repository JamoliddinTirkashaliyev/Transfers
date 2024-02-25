from django.contrib import admin
from django.urls import path

from mainApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='home'),
                  path('clubs/', clubs, name='clubs'),
                  path('stats/', stats, name='stats'),
                  path('palyers/', players, name='players'),
                  path('about/', about, name='about'),
                  path('lastest_transfers/', lastest_transfers, name='lastest_transfers'),
                  path('clubs/', clubs, name='clubs'),
                  path('players20/', u_20, name='u_20'),
                  path('tryouts/', tryouts, name='tryouts'),
                  path('archive/', transfer_archive, name='archive'),
                  path('season/', season2017_18, name='season2017_18'),
                  path('season/', season2018_19, name='season2018_19'),
                  path('season/', season2019_20, name='season2019_20'),
                  path('season/', season2020_21, name='season2020_21'),
                  path('transfer_records/', transfer_records),
                  path('<str:country_name>/clubs/', country_clubs),
                  path('<str:nom>/players/', clubs_players),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
