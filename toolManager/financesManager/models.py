from django.db import models

#TODO: Update

class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=120)
    localidad = models.CharField(max_length=20,blank=True)
    codigoPostal = models.CharField(max_length=11,blank=True)

class PedidoProveedor(models.Model):
    nombre = models.CharField(max_length=30)
    referencia = models.CharField(max_length=10)
    fechaPedido = models.DateField()
    fechaEntrega = models.DateField(null=True,blank=True)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.SET_NULL,null=True)
    #pedidoCliente

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=120,blank=True)
    identificador = models.CharField(max_length=11,blank=True,null=True)
    direccion = models.CharField(max_length=80,blank=True,null=True)
    pais = models.CharField(max_length=12,blank=True,null=True)
    iban = models.CharField(max_length=33,blank=True,null=True)
    telefono = models.CharField(max_length=11,blank=True,null=True)
    email = models.CharField(max_length=40,blank=True,null=True)

class Presupuesto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=120,blank=True)
    fechaPedido = models.DateField()
    fechaTope = models.DateField(blank=True,null=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)

class ItemPresupuesto(models.Model):
    presupuesto = models.ForeignKey(Presupuesto,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=80,blank=True)
    cantidad = models.IntegerField()
    precioUnitario = models.IntegerField(blank=True,null=True)
    precioTotal = models.IntegerField()
    fechaTope = models.IntegerField(blank=True,null=True)


class PedidoCliente(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=120,blank=True)
    fechaPedido = models.DateField()
    fechaTope = models.DateField(blank=True,null=True)
    fechaEntrega = models.DateField(blank=True,null=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.SET_NULL,null=True)
    presupuesto = models.ForeignKey(Presupuesto,on_delete=models.SET_NULL,null=True)

class ItemPedido(models.Model):
    pedidoCliente = models.ForeignKey(PedidoCliente,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=80,blank=True)
    cantidad = models.IntegerField()
    precioUnitario = models.IntegerField(blank=True,null=True)
    precioTotal = models.IntegerField()
    fechaTope = models.IntegerField(blank=True,null=True)

class Albaran(models.Model):
    pedidoCliente = models.ForeignKey(PedidoCliente,on_delete=models.CASCADE)
    datos = models.JSONField()
    fechaAlbaran = models.DateField()

class ItemAlbaran(models.Model):
    albaran = models.ForeignKey(Albaran,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=80,blank=True)
    cantidad = models.IntegerField()
    precioUnitario = models.IntegerField(blank=True,null=True)
    precioTotal = models.IntegerField()
    fechaTope = models.IntegerField(blank=True,null=True)

class FacturaPedido(models.Model):
    albaran = models.ForeignKey(Albaran,on_delete=models.CASCADE)
    datos = models.JSONField()
    fechaFactura = models.DateField()
