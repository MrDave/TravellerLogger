from django.shortcuts import render
from planets.models import Planet
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def index(request):
    return JsonResponse({"Welcome": "to Traveller Logger"})


def planet_list(request):
    planets = Planet.objects.all()
    response = {
        "planets": [
            {
                "id": planet.id,
                "name": planet.name,
                "planet_coords": planet.planet_coords,
                "wiki_link": planet.wiki_link
            } for planet in planets
        ]
    }

    return JsonResponse(response, json_dumps_params={"ensure_ascii": False, "indent": 2})


def planet_details(request, planet_id):
    planet = get_object_or_404(Planet, id=planet_id)
    map_render_link = f"https://travellermap.com/api/jumpmap?sector=Trojan+Reach&hex={planet.planet_coords}&jump=3"
    response = {
        "name": planet.name,
        "coordinates": planet.planet_coords,
        "wiki_link": planet.wiki_link,
        "map_render_link": map_render_link
    }
    return JsonResponse(response, json_dumps_params={"ensure_ascii": False, "indent": 2})
