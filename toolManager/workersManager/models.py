from django.db import models
from financesManager.models import ClientOrder

class Project(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=200,blank=True, null=True)
    clientOrder = models.ForeignKey(ClientOrder,blank=True, null=True, on_delete=models.SET_NULL)

class Worker(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120,blank=True, null=True)
    iban = models.CharField(max_length=11, blank=True, null=True)
    phoneNumber = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    projects = models.ManyToManyField(Project,blank=True, null=True)