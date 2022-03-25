from django.db import models
from financesManager.models import SupplierOrder


class Materials(models.Model):
    innerName = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)


class Machine(models.Model):
    name = models.CharField(max_length=20)
    workspaceLimitX = models.FloatField(null=True, blank=True)
    workspaceLimitY = models.FloatField(null=True, blank=True)
    workspaceLimitZ = models.FloatField(null=True, blank=True)
    maxSpeed = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    data = models.JSONField(null=True, blank=True)
    materials = models.ManyToManyField(Materials)

    def __str__(self) -> str:
        return self.name


class ToolArchetype(models.Model):
    name = models.CharField(max_length=20, unique=True)
    cuttingDiameter = models.FloatField(default=0)
    handleDiameter = models.FloatField(default=0)
    cuttingLength = models.FloatField(default=0)
    length = models.FloatField(default=0)
    blades = models.IntegerField(default=1)
    data = models.JSONField(null=True, blank=True)
    materials = models.ManyToManyField(Materials)
    relaction = models.ManyToManyField(Machine, through="ArchetypeMachineRelation")

    def __str__(self) -> str:
        return self.name


class ArchetypeMachineRelation(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    toolArchetype = models.ForeignKey(ToolArchetype, on_delete=models.CASCADE)
    speed = models.FloatField()
    F = models.FloatField()  # TODO


class Tool(models.Model):
    name = models.CharField(max_length=20)
    toolArchetype = models.ForeignKey(ToolArchetype, on_delete=models.SET_NULL, null=True)
    supplierOrder = models.ForeignKey(SupplierOrder, blank=True, on_delete=models.SET_NULL, null=True)
    cuttingDiameter = models.FloatField(default=0)
    handleDiameter = models.FloatField(default=0)
    cuttingLength = models.FloatField(default=0)
    length = models.FloatField(default=0)
    blades = models.IntegerField(default=1)
    data = models.JSONField(null=True, blank=True)
    dateEntry = models.DateField()
    dateScrap = models.DateField(null=True, blank=True)
    reference = models.CharField(max_length=10)
    hours = models.IntegerField(blank=True, default=0)
    stockPlace = models.CharField(max_length=15, blank=True, null=True)
    materials = models.ManyToManyField(Materials)
    asignedMachine = models.ForeignKey(Machine, on_delete=models.SET_NULL, null=True)
    speed = models.FloatField()
    F = models.FloatField()

    def __str__(self) -> str:
        return self.name
