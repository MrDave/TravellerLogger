from django.contrib import admin
from planets.models import Planet


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    pass
