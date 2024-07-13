from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Planet(models.Model):
    name = models.CharField(max_length=20, verbose_name="planet name")
    planet_coords = models.CharField(max_length=4, blank=True)
    wiki_link = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Ware(models.Model):
    name = models.CharField(max_length=50)
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
        null=True
    )
    sell_price = models.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(400)],
        verbose_name="sell price, %",
        blank=True,
        null=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["planet", "ware"],
                name="unique_wares_for_planets"
            ),
            models.CheckConstraint(
                name="purchase_or_sell_price_check",
                check=(
                    models.Q(purchase_price__isnull=False)
                    | models.Q(sell_price__isnull=False)
                ),
                violation_error_message="At least one of the prices should be filled"
            )
        ]

    def __str__(self):
        return f"{self.ware} - {self.planet}"
