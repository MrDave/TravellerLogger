from django.contrib import admin
from planets.models import Planet, PlanetWare, Ware, MapSector


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    pass


@admin.register(Ware)
class WareAdmin(admin.ModelAdmin):
    pass


@admin.register(PlanetWare)
class PlanetWareAdmin(admin.ModelAdmin):
    pass


@admin.register(MapSector)
class MapSectorAdmin(admin.ModelAdmin):
    pass