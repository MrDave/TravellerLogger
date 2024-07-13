from django.shortcuts import render, get_object_or_404
from planet_economy.models import Planet, Ware
from django.http import JsonResponse
from django.contrib.auth import get_user_model


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
        "jump_link": f"https://travellermap.com/api/jumpmap?sector=Trojan+Reach&hex={planet.planet_id}&jump=3",
        "wares": planet.wares.all().prefetch_related("ware")
    }
    return render(request, "planet_details.html", context)


def wares_list(request):
    wares = Ware.objects.prefetch_related("planets")
    context = {
        "wares": wares
    }
    return render(request, "wares.html", context)


# def index(request):
#     user = request.user
#
#     render(request, "base.html")
