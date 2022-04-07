
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.archetypesView, name="toolsView"),
    path("archetypes/view/", views.archetypesView, name="archetypesView"),
    path("archetypes/create/", views.archetypesCreate, name="archetypesCreate"),
    path("machines/view/", views.machinesView, name="machinesView"),
    path("machines/create/", views.machinesCreate, name="machinesCreate"),
]
