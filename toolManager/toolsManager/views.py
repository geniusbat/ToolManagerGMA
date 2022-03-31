import json
from django.shortcuts import render
from .models import ArchetypeMachineRelation, Machine, Materials, ToolArchetype

#TODO: Get data as json from api

def machinesView(request):
    template = "toolsManager/machinesView.html"
    materialNames = Materials.objects.all().values_list("name",flat=True)
    materialInnerNames = Materials.objects.all().values_list("innerName",flat=True)
    materialsData = dict(zip(materialInnerNames,materialNames))
    archetypes = dict(ToolArchetype.objects.all().values())
    archetypesData = {}
    for id, archetype in archetypes.items():
        data={}
        for field, value in archetype.items():
            data[field]=value
        #Get data dependent on machine
        data.pop("relation",None)
        data["machines"]={}
        for relationId in archetype["relation"]:
            relation = ArchetypeMachineRelation.objects.filter(id=relationId)
            data["machines"][Machine.objects.filter(id=relation.machine)]={"speed":relation["speed"],"F":relation["F"]}
        archetypesData[id]=data
    context = {}
    context["materialsData"]=json.dumps(materialsData)
    context["archetypesData"]=json.dumps(archetypesData)
    #TODO: Proveedores
    #context["proveedoresData"]=json.dumps(proveedoresData)
    return render(request, template, context)