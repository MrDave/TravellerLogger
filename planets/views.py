from django.shortcuts import render
from planets.models import Planet
from django.http import JsonResponse


def planet_list(request):
    planets = Planet.objects.all()
    response = {
        "planets": [{"id": planet.id, "name": planet.name, "planet_coords": planet.planet_coords, "wiki_link": planet.wiki_link} for planet in planets]
    }

    return JsonResponse(response, json_dumps_params={"ensure_ascii": False, "indent": 2})


def index(request):
    return JsonResponse({"Welcome": "to Traveller Logger"})

