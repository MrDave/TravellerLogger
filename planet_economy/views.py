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
    planet = get_object_or_404(Planet, planet_id=planet_id)
    payload = {
        "name": planet.name,
        "planet_id": planet.planet_id,
        "wiki_link": planet.wiki_link
    }
    return JsonResponse(payload)
