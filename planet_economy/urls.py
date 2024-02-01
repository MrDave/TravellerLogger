from django.urls import path
from planet_economy import views

app_name = "planet_economy"

urlpatterns = [
    path("<int:planet_id>", views.planet_details, name="planet_details"),
    path("", views.planet_list, name="planet_list")
]
