from django.views.generic import ListView
from planets.models import Planet


class PlanetListView(ListView):
    model = Planet
    context_object_name = "planet_list"
