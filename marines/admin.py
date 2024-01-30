from django.contrib import admin
from marines.models import Hireling


@admin.register(Hireling)
class HirelingAdmin(admin.ModelAdmin):
    pass
