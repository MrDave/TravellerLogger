from django.contrib import admin
from planet_economy.models import Planet, PlanetWare, Ware


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    pass


@admin.register(PlanetWare)
class PlanetWareAdmin(admin.ModelAdmin):
    pass


@admin.register(Ware)
class WareAdmin(admin.ModelAdmin):
    pass
