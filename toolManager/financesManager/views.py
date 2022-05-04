from .models import *
from django.core import serializers
from django.shortcuts import redirect, render

#CLIENTS ORDERS

def clientOrdersView(request):
    template = "baseTemplates/genericView.html"
    context = {}
    context["viewData"] = {}; context["viewData"]["title"] = "Tools"
    context["viewData"]["fields"] = [ClientOrder._meta.get_field(field).verbose_name for field in ClientOrder.getFieldNames()]
    context["viewData"]["viewUrl"] = "toolsView"
    context["viewData"]["createUrl"] = "toolsCreate"
    context["viewData"]["updateUrl"] = "toolsUpdate"
    context["viewData"]["deleteUrl"] = "toolsDelete"
    data = serializers.serialize( "python", ClientOrder.objects.all(), fields=ClientOrder.getFieldNames())
    context["viewModels"] = data
    return render(request, template, context)