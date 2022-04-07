import json
from django.shortcuts import redirect, render
from django.core import serializers
from .models import ArchetypeMachineRelation, Machine, Materials, ToolArchetype
from .forms import * 

#TODO: Use instead api json

#TOOLS

def archetypesView(request):
    template = "toolsManager/genericView.html"
    context = {}
    context["viewData"] = {}; context["viewData"]["title"] = "Tool Archetypes"
    context["viewData"]["fields"] = [ToolArchetype._meta.get_field(field).verbose_name for field in ToolArchetype.getFieldNames()]
    data = serializers.serialize( "python", ToolArchetype.objects.all(), fields=ToolArchetype.getFieldNames())
    context["viewModels"] = data
    return render(request, template, context)

def archetypesCreate(request):
    #Create machine
    if request.method == "POST":
        form = ArchetypesForm(request.POST)
        if form.is_valid():
            form.save()
            print("Archetype  was saved")
            return redirect("archetypesView")
    #Generate view 
    else:
        template = "toolsManager/archetypesCreate.html"
        context = {}
        formData = {}
        formData["title"] = "Create Archetype Tool"
        form = ArchetypesForm()
        context = {"form":form,"formData":formData}; context["machines"] = list(Machine.objects.all().values_list('name', flat=True))
        return render(request, template, context)

#MACHINES

def machinesView(request):
    template = "toolsManager/genericView.html"
    context = {}
    context["viewData"] = {}; context["viewData"]["title"] = "Machines"
    context["viewData"]["fields"] = [Machine._meta.get_field(field).verbose_name for field in Machine.getFieldNames()]
    data = serializers.serialize( "python", Machine.objects.all(), fields=Machine.getFieldNames())
    context["viewModels"] = data
    return render(request, template, context)

def machinesCreate(request):
    #Create machine
    if request.method == "POST":
        machineForm = MachinesForm(request.POST)
        if machineForm.is_valid():
            machineForm.save()
            print("Machine  was saved")
            return redirect("machinesView")
    #Generate view 
    else:
        template = "toolsManager/genericForm.html"
        context = {}
        formData = {}
        formData["title"] = "Create Machine"
        machineForm = MachinesForm()
        context = {"form":machineForm,"formData":formData}
        return render(request, template, context)
