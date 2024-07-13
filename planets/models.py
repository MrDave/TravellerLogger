from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=20, verbose_name="planet name")
    planet_id = models.CharField(max_length=4, blank=True)
    wiki_link = models.TextField()

    def __str__(self):
        return self.name


class Ware(models.Model):
    pass

