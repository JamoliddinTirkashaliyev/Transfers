from .models import *


def countries(request):
    davlatlar = Davlat.objects.all()
    if len(davlatlar) % 2 == 0:
        countries1 = davlatlar[:len(davlatlar) // 2]
        countries2 = davlatlar[len(davlatlar) // 2:]
    else:
        countries1 = davlatlar[:(len(davlatlar) + 1) // 2]
        countries2 = davlatlar[(len(davlatlar) + 1) // 2:]
    context = {
        'countries1': countries1,
        'countries2': countries2,
    }
    return context
