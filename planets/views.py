from django.views.generic import DetailView, ListView
from planets.models import Planet


class PlanetListView(ListView):
    model = Planet
    context_object_name = "planet_list"


class PlanetDetailView(DetailView):
    model = Planet
    context_object_name = "planet"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: add PlanetWares context
        return context
