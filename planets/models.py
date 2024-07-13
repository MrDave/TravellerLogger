from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=20, verbose_name="planet name")
    planet_coords = models.CharField(max_length=4, blank=True)
    wiki_link = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Ware(models.Model):
    pass

