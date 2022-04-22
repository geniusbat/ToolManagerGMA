
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.toolsView, name="toolsView"),
    path("create/", views.toolsCreate, name="toolsCreate"),
    path("update/<int:id>", views.toolsUpdate, name="toolsUpdate"),
    path("delete/<int:id>", views.toolsDelete, name="toolsDelete"),
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
