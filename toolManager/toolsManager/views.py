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
        print("FFFFFFFFFFFFFFFFF")
        if form.is_valid():
            form.save()
            print("Archetype  was saved")
            print(form.data)
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
        form = MachinesForm(request.POST)
        if form.is_valid():
            form.save()
            print("Machine  was saved")
            print(form.data)
            return redirect("machinesView")
    #Generate view 
    else:
        template = "toolsManager/genericForm.html"
        context = {}
        formData = {}
        formData["title"] = "Create Machine"
        form = MachinesForm()
        context = {"form":form,"formData":formData}
        return render(request, template, context)

def machinesUpdate(request, id):
    #Update Machine
    if request.method == "POST":
        form = MachinesForm(request.POST)
        if form.is_valid():
            form.save()
            print("Machine  was updated")
            print(form.data)
            return redirect("machinesView")
    #Generate view 
    else:
        template = "toolsManager/genericForm.html"
        context = {}
        formData = {}
        formData["title"] = "Create Machine"
        object = Machine.objects.get(id=id)
        form = MachinesForm(instance=object)
        context = {"form":form,"formData":formData}
        return render(request, template, context)


#MATERIALS

def materialsView(request):
    template = "toolsManager/genericView.html"
    context = {}
    context["viewData"] = {}; context["viewData"]["title"] = "Materials"
    context["viewData"]["fields"] = [Materials._meta.get_field(field).verbose_name for field in Materials.getFieldNames()]
    data = serializers.serialize( "python", Materials.objects.all(), fields=Materials.getFieldNames())
    context["viewModels"] = data
    return render(request, template, context)

def materialsCreate(request):
    #Create material
    if request.method == "POST":
        form = MaterialsForm(request.POST)
        if form.is_valid():
            form.save()
            print("Material  was saved")
            print(form.data)
            return redirect("materialsView")
    #Generate view 
    else:
        template = "toolsManager/genericForm.html"
        context = {}
        formData = {}
        formData["title"] = "Create Material"
        form = MaterialsForm()
        context = {"form":form,"formData":formData}
        return render(request, template, context)

def materialsUpdate(request, id):
    #Update material
    if request.method == "POST":
        form = MaterialsForm(request.POST)
        if form.is_valid():
            form.save()
            print("Material  was updated")
            print(form.data)
            return redirect("materialsView")
    #Generate view 
    else:
        template = "toolsManager/genericForm.html"
        context = {}
        formData = {}
        formData["title"] = "Create Material"
        object = Materials.objects.get(id=id)
        form = MaterialsForm(instance=object)
        context = {"form":form,"formData":formData}
        return render(request, template, context)