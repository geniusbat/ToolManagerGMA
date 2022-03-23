from django.db import models

#TODO: Update

class ToolArchetype(models.Model):
    nombre = models.CharField(max_length=20,unique=True)
    DC = models.FloatField()
    DM = models.FloatField()
    R = models.FloatField()
    LC = models.FloatField()
    LR = models.FloatField()
    L = models.FloatField()
    Z = models.IntegerField()
    material = ArrayField(models.CharField(max_length=13,choices=MATERIALS))
    relacion = models.ManyToManyField(Maquina,through="RelacionArquetipoMaquina")
    def __str__(self) -> str:
        return self.nombre

class Tool(models.Model):
    nombre = models.CharField(max_length=20)
    arquetipo = models.ForeignKey(Arquetipo,on_delete=models.SET_NULL,null=True)
    pedidoProveedor = models.ForeignKey(PedidoProveedor,blank=True,on_delete=models.SET_NULL,null=True)
    DC = models.FloatField()
    DM = models.FloatField()
    R = models.FloatField()
    LC = models.FloatField()
    LR = models.FloatField()
    L = models.FloatField()
    Z = models.IntegerField()
    fechaEntrada = models.DateField()
    fechaScrap = models.DateField(null=True,blank=True)
    referencia = models.CharField(max_length=10)
    horasUso = models.IntegerField(blank=True,default=0)
    almacen = models.CharField(max_length=15)
    material = ArrayField(models.CharField(max_length=13,choices=MATERIALS))
    maquinaAsignada = models.ForeignKey(Maquina, on_delete=models.SET_NULL,null=True)
    S = models.FloatField()
    F = models.FloatField()
    extras = JSONField(blank=True)
    def __str__(self) -> str:
        return self.nombre

class ArchetypeMachineRelation(models.Model):
    maquina = models.ForeignKey(Maquina,on_delete=models.CASCADE)
    arquetipo = models.ForeignKey(Arquetipo,on_delete=models.CASCADE)
    S = models.FloatField()
    F = models.FloatField()