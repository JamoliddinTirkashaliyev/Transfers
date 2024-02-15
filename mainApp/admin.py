from django.contrib import admin
from .models import *


admin.site.register(Davlat)

class ClubAdmin(admin.ModelAdmin):
    list_display = ('nom', 'murabbiy', 'davlat')
    search_fields = ['nom']
    list_filter = ['davlat']


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('ism', 'club', 'narx', 'davlat')
    search_fields = ['nom']
    list_filter = ['club']
    autocomplete_fields = ['club']



class TransferAdmin(admin.ModelAdmin):
    list_display = ('player', 'club_eski', 'club_yangi', 'narx')


admin.site.register(Club, ClubAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Transfer, TransferAdmin)
