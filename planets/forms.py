from django.forms import ModelForm
from planets.models import PlanetWare


class PlanetWareForm(ModelForm):
    class Meta:
        model = PlanetWare
        fields = ["ware", "purchase_price", "sell_price"]

