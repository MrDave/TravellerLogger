from django.shortcuts import render
from planets.models import Planet, PlanetWare
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory, BaseInlineFormSet
from django.conf import settings
from planets.helper_functions import build_jump_map_link


def index(request):
    return JsonResponse({"Welcome": "to Traveller Logger"})


# TODO: write normal views and move API views to API app
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
    map_render_link = build_jump_map_link(planet.sector, planet.planet_coords, **settings.TRAVELLER_API_CONFIG)
    wares_list = planet.wares.all().prefetch_related("ware")
    response = {
        "name": planet.name,
        "coordinates": planet.planet_coords,
        "wiki_link": planet.wiki_link,
        "map_render_link": map_render_link,
        "wares_list": [
            {"name": pware.ware.name, "purchase price": pware.purchase_price, "sell price": pware.sell_price}
            for pware in wares_list
        ]
    }
    return JsonResponse(response, json_dumps_params={"ensure_ascii": False, "indent": 2})


def planet_form_details(request, planet_id):
    planet = get_object_or_404(Planet, pk=planet_id)
    wares_list = planet.wares.all().prefetch_related("ware").order_by("ware__name")

    queryset = PlanetWare.objects.order_by("ware__name")

    PlanetWareInlineFormSet = inlineformset_factory(
        Planet,
        PlanetWare,
        fields=["ware", "purchase_price", "sell_price"],
        extra=1
    )

    map_render_link = build_jump_map_link(planet.sector, planet.planet_coords, **settings.TRAVELLER_API_CONFIG)

    if request.method == "POST":
        formset = PlanetWareInlineFormSet(request.POST, queryset=queryset, instance=planet)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(planet.get_absolute_url())

    else:
        formset = PlanetWareInlineFormSet(queryset=queryset, instance=planet)
    context = {
        "planet": planet,
        "wares_list": wares_list,
        "map_render_link": map_render_link,
        "formset": formset,
    }
    return render(request, "planet_details.html", context)
