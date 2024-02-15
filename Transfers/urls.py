from django.contrib import admin
from django.urls import path

from mainApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('clubs/', clubs, name='clubs'),
    path('palyers/', players, name='players'),
    path('lastest_transfers/', lastest_transfers, name='lastest_transfers'),
    path('clubs/', clubs, name='clubs'),
    path('transfer_records/', transfer_records),
    path('<str:country_name>/clubs/',country_clubs),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
