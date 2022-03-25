from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=30)
    iban = models.CharField(max_length=11, blank=True, null=True)
    phoneNumber = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)

class Project(models.Model):
    pass
