import json
from django.shortcuts import redirect, render
from django.core import serializers
from .forms import *

#TOOLS

def toolsView(request):
    template = "toolsManager/toolsManagerView.html"
    context = {}
    context["viewData"] = {}; context["viewData"]["title"] = "Tools"
    context["viewData"]["fields"] = [Tool._meta.get_field(field).verbose_name for field in Tool.getFieldNames()]
    context["viewData"]["viewUrl"] = "toolsView"
    context["viewData"]["createUrl"] = "toolsCreate"
    context["viewData"]["updateUrl"] = "toolsUpdate"
    context["viewData"]["deleteUrl"] = "toolsDelete"
    data = serializers.serialize( "python", Tool.objects.all(), fields=Tool.getFieldNames())
    context["viewModels"] = data
    return render(request, template, context)

def toolsCreate(request):
    #Create machine
    if request.method == "POST":
        form = ToolsForm(request.POST)
        if form.is_valid():
            form.save()
            print("Tool  was saved")
            print(form.data)
            return redirect("toolsView")
    #Generate view
    else:
        template = "toolsManager/toolsManagerForm.html"
        formData = {}
        formData["title"] = "Create Tool"
        form = ToolsForm()
        context = {"form":form,"formData":formData}
        context["formData"]["viewUrl"] = "toolsView"
        context["formData"]["createUrl"] = "toolsCreate"
        context["formData"]["updateUrl"] = "toolsUpdate"
        context["formData"]["deleteUrl"] = "toolsDelete"
        return render(request, template, context)

def toolsUpdate(request, id):
    print(request.method)
    #Update Machine
    if request.method == "POST":
        form = ToolsForm(request.POST, instance=Tool.objects.get(id=id))
        if form.is_valid():
            form.save()
            print("Tool  was updated")
            print(form.data)
            return redirect("toolsView")
    #Generate view
    else:
        template = "toolsManager/toolsManagerForm.html"
        formData = {}
        formData["title"] = "Edit Tool"
        obj = Tool.objects.get(id=id)
        form = ToolsForm(instance=obj)
        context = {"form":form,"formData":formData}
        context["formData"]["viewUrl"] = "toolsView"
        context["formData"]["createUrl"] = "toolsCreate"
        context["formData"]["updateUrl"] = "toolsUpdate"
        context["formData"]["deleteUrl"] = "toolsDelete"
        return render(request, template, context)

def toolsDelete(request, id):
    Tool.objects.filter(id=id).delete()
    return redirect("toolsView")


#MACHINES

def machinesView(request):
    template = "toolsManager/toolsManagerView.html"
    context = {}
    context["viewData"] = {}; context["viewData"]["title"] = "Machines"
    context["viewData"]["fields"] = [Machine._meta.get_field(field).verbose_name for field in Machine.getFieldNames()]
    context["viewData"]["viewUrl"] = "machinesView"
    context["viewData"]["createUrl"] = "machinesCreate"
    context["viewData"]["updateUrl"] = "machinesUpdate"
    context["viewData"]["deleteUrl"] = "machinesDelete"
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
        template = "toolsManager/toolsManagerForm.html"
        formData = {}
        formData["title"] = "Create Machine"
        form = MachinesForm()
        context = {"form":form,"formData":formData}
        context["formData"]["viewUrl"] = "machinesView"
        context["formData"]["createUrl"] = "machinesCreate"
        context["formData"]["updateUrl"] = "machinesUpdate"
        context["formData"]["deleteUrl"] = "machinesDelete"
        return render(request, template, context)

def machinesUpdate(request, id):
    #Update Machine
    if request.method == "POST":
        form = MachinesForm(request.POST, instance=Machine.objects.get(id=id))
        if form.is_valid():
            form.save()
            print("Machine  was updated")
            print(form.data)
            return redirect("machinesView")
    #Generate view 
    else:
        template = "toolsManager/toolsManagerForm.html"
        context = {}
        formData = {}
        formData["title"] = "Update Machine"
        object = Machine.objects.get(id=id)
        form = MachinesForm(instance=object)
        context = {"form":form,"formData":formData}
        context["formData"]["viewUrl"] = "machinesView"
        context["formData"]["createUrl"] = "machinesCreate"
        context["formData"]["updateUrl"] = "machinesUpdate"
        context["formData"]["deleteUrl"] = "machinesDelete"
        return render(request, template, context)

def machinesDelete(request, id):
    Machine.objects.filter(id=id).delete()
    return redirect("machinesView")


#MATERIALS

def materialsView(request):
    template = "toolsManager/toolsManagerView.html"
    context = {}
    context["viewData"] = {}; context["viewData"]["title"] = "Materials"
    context["viewData"]["fields"] = [Materials._meta.get_field(field).verbose_name for field in Materials.getFieldNames()]
    context["viewData"]["viewUrl"] = "materialsView"
    context["viewData"]["createUrl"] = "materialsCreate"
    context["viewData"]["updateUrl"] = "materialsUpdate"
    context["viewData"]["deleteUrl"] = "materialsDelete"
    data = serializers.serialize( "python", Materials.objects.all(), fields=Materials.getFieldNames())
    print(data)
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
        template = "toolsManager/toolsManagerForm.html"
        context = {}
        formData = {}
        formData["title"] = "Create Material"
        form = MaterialsForm()
        context = {"form":form,"formData":formData}
        context["formData"]["viewUrl"] = "materialsView"
        context["formData"]["createUrl"] = "materialsCreate"
        context["formData"]["updateUrl"] = "materialsUpdate"
        context["formData"]["deleteUrl"] = "materialsDelete"
        return render(request, template, context)

def materialsUpdate(request, id):
    #Update material
    if request.method == "POST":
        form = MaterialsForm(request.POST, instance=Materials.objects.get(id=id))
        if form.is_valid():
            form.save()
            print("Material  was updated")
            print(form.data)
            return redirect("materialsView")
    #Generate view 
    else:
        template = "toolsManager/toolsManagerForm.html"
        context = {}
        formData = {}
        formData["title"] = "Update Material"
        object = Materials.objects.get(id=id)
        form = MaterialsForm(instance=object)
        context = {"form":form,"formData":formData}
        context["formData"]["viewUrl"] = "materialsView"
        context["formData"]["createUrl"] = "materialsCreate"
        context["formData"]["updateUrl"] = "materialsUpdate"
        context["formData"]["deleteUrl"] = "materialsDelete"
        return render(request, template, context)

def materialsDelete(request, id):
    Materials.objects.filter(id=id).delete()
    return redirect("materialsView")