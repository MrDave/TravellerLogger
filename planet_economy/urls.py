from django.urls import path
from planet_economy import views

app_name = "planet_economy"

urlpatterns = [
    path("", views.planet_list)
]
