from django.shortcuts import render
from planet_economy.models import Planet


def planet_list(request):
    planets = Planet.objects.all()
    context = {
        "planets": planets
    }
    return render(request, "planets.html", context)
