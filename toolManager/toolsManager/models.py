from django.db import models
from financesManager.models import SupplierOrder


class Materials(models.Model):
    name = models.CharField(max_length=20)
    def getFieldNames() -> list:
        return ["name"]
    def notRequiredFields() -> list:
        return []


class Machine(models.Model):
    name = models.CharField(max_length=20)
    workspaceLimitX = models.FloatField(null=True, blank=True, verbose_name="Workspace Limit X")
    workspaceLimitY = models.FloatField(null=True, blank=True, verbose_name="Workspace Limit Y")
    workspaceLimitZ = models.FloatField(null=True, blank=True, verbose_name="Workspace Limit Z")
    maxSpeed = models.FloatField(null=True, blank=True, verbose_name="Max Speed")
    precision = models.FloatField(null=True, blank=True)
    data = models.JSONField(null=True, blank=True)
    materials = models.ManyToManyField(Materials)
    def getFieldNames() -> list:
        return ["name","workspaceLimitX","workspaceLimitY","workspaceLimitZ","maxSpeed","precision","data","materials"]
    def notRequiredFields() -> list:
        return ["maxSpeed","precision","data","materials"] #TODO: Remove materials
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
    relation = models.ManyToManyField(Machine, through="ArchetypeMachineRelation")
    def getFieldNames() -> list:
        return ["name","cuttingDiameter","handleDiameter","cuttingLength","length","blades","data","materials","relation"]
    def notRequiredFields() -> list:
        return ["data","handleDiameter","materials"] #TODO: Remove materials
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
