
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.archetypesView, name="toolsView"),
    path("archetypes/view/", views.archetypesView, name="archetypesView"),
    path("archetypes/create/", views.archetypesCreate, name="archetypesCreate"),
    path("machines/view/", views.machinesView, name="machinesView"),
    path("machines/create/", views.machinesCreate, name="machinesCreate"),
    path("machines/update/<int:id>", views.machinesUpdate, name="machinesUpdate"),
    path("materials/view/", views.materialsView, name="materialsView"),
    path("materials/create/", views.materialsCreate, name="materialsCreate"),
    path("materials/update/<int:id>", views.materialsUpdate, name="materialsUpdate"),
]
