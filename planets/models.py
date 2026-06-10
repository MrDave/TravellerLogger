from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from urllib import parse
from planets.helper_functions import build_jump_map_link


MAP_BASE_LINK = "https://travellermap.com/go/"

class MapSector(models.Model):
    name = models.CharField(max_length=20, verbose_name="sector name")

    def __str__(self):
        return self.name


class Planet(models.Model):
    name = models.CharField(max_length=20, verbose_name="planet name")
    sector = models.ForeignKey(MapSector, on_delete=models.CASCADE)
    planet_coordinates = models.CharField(max_length=4, blank=True)
    wiki_link = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("planet_details", kwargs={"planet_id": self.pk})

    def map_link(self):
        return parse.urljoin(MAP_BASE_LINK, f"{self.sector}/{self.planet_coordinates}")

    def map_render_link(self):
        return build_jump_map_link(self.sector.name, str(self.planet_coordinates), **settings.TRAVELLER_API_CONFIG)

    def __str__(self):
        return self.name


class Ware(models.Model):
    name = models.CharField(max_length=50, unique=True)
    base_price = models.DecimalField(decimal_places=3, max_digits=8, verbose_name="base cost, kCr")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class PlanetWare(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name="wares")
    ware = models.ForeignKey(Ware, on_delete=models.CASCADE, related_name="planets")
    purchase_price = models.IntegerField(
        validators=[MinValueValidator(15), MaxValueValidator(300)],
        verbose_name="purchase price, %",
        blank=True,
        null=True,
    )
    sell_price = models.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(400)],
        verbose_name="sell price, %",
        blank=True,
        null=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["planet", "ware"],
                name="unique_wares_for_planets",
            ),
            models.CheckConstraint(
                name="purchase_or_sell_price_check",
                condition=(
                    models.Q(purchase_price__isnull=False)
                    | models.Q(sell_price__isnull=False)
                ),
                violation_error_message="At least one of the prices should be filled",
            ),
        ]

    def __str__(self):
        return f"{self.ware} - {self.planet}"
