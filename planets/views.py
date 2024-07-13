from django.shortcuts import render
from planets.models import Planet
from django.http import JsonResponse


def planet_list(request):
    planets = Planet.objects.all()
    response = {
        "planets": [{"name": planet.name, "planet_id": planet.planet_id, "wiki_link": planet.wiki_link} for planet in planets]
    }

    return JsonResponse(response, json_dumps_params={"ensure_ascii": False, "indent": 4})


def index(request):
    return JsonResponse({"Welcome": "to Traveller Logger"})

