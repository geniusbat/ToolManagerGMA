
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.archetypesView, name="toolsView"),
    path("archetypes/", views.archetypesView),
    path("archetypes/view/", views.archetypesView, name="archetypesView"),
    path("archetypes/create/", views.archetypesCreate, name="archetypesCreate"),
    path("archetypes/delete/<int:id>", views.archetypesDelete, name="archetypesDelete"),
    path("machines/", views.machinesView),
    path("machines/view/", views.machinesView, name="machinesView"),
    path("machines/create/", views.machinesCreate, name="machinesCreate"),
    path("machines/update/<int:id>", views.machinesUpdate, name="machinesUpdate"),
    path("machines/delete/<int:id>", views.machinesDelete, name="machinesDelete"),
    path("materials/", views.materialsView),
    path("materials/view/", views.materialsView, name="materialsView"),
    path("materials/create/", views.materialsCreate, name="materialsCreate"),
    path("materials/update/<int:id>", views.materialsUpdate, name="materialsUpdate"),
    path("materials/delete/<int:id>", views.materialsDelete, name="materialsDelete"),
]
