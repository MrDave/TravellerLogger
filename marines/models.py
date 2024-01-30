from django.db import models


class Hireling(models.Model):
    name = models.CharField(max_length=50)
    dei = models.SmallIntegerField(verbose_name="DEI")
    primary_skills = models.CharField(max_length=100)
    secondary_skills = models.CharField(max_length=100, blank=True)
    cost = models.IntegerField(verbose_name="hire cost")
    gear = models.CharField(max_length=50, blank=True)
    is_alive = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
