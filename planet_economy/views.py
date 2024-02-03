from django.shortcuts import render, get_object_or_404
from planet_economy.models import Planet
from django.http import JsonResponse


def planet_list(request):
    planets = Planet.objects.all()
    context = {
        "planets": planets
    }
    return render(request, "planets.html", context)


def planet_details(request, planet_id):
    planet = get_object_or_404(Planet, id=planet_id)
    context = {
        "planet": planet,
        "wares": planet.wares.all().prefetch_related("ware")
    }
    return render(request, "planet_details.html", context)

