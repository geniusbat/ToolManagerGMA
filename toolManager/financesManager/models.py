from django.db import models

class AddressableMixin(models.Model):
    class Meta:
        abstract=True
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=20,blank=True,null=True)
    zipCode = models.CharField(max_length=11,blank=True,null=True)
    country = models.CharField(max_length=12,blank=True,null=True)

class ContactableMixin(models.Model):
    class Meta:
        abstract=True
    personName = models.CharField(max_length=30)
    personIdentification = models.CharField(max_length=11,blank=True,null=True)
    phoneNumber = models.CharField(max_length=11,blank=True,null=True)
    email = models.CharField(max_length=40,blank=True,null=True)

class Client(AddressableMixin, ContactableMixin):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120,blank=True,null=True)
    iban = models.CharField(max_length=33,blank=True,null=True)

class ClientOrder(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120,blank=True,null=True)
    dateOrder = models.DateField()
    dateTop = models.DateField(blank=True,null=True)
    dateDelivery = models.DateField(blank=True,null=True)
    client = models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)

class ItemClientOrder(models.Model):
    clientOrder = models.ForeignKey(ClientOrder,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=80,blank=True,null=True)
    quantity = models.IntegerField(default=1)
    priceUnitary = models.IntegerField(blank=True,null=True)
    priceTotal = models.IntegerField()
    dateTop = models.IntegerField(blank=True,null=True)

class ClientInvoice(models.Model):
    clientOrder = models.ForeignKey(ClientOrder,on_delete=models.CASCADE)
    data = models.JSONField(null=True,blank=True)
    dateInvoice = models.DateField()

class Supplier(AddressableMixin, ContactableMixin):
    name = models.CharField(max_length=30)

class SupplierOrder(models.Model):
    name = models.CharField(max_length=30)
    reference = models.CharField(max_length=10)
    dateOrder = models.DateField()
    dateDelivery = models.DateField(null=True,blank=True)
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True)
    clientOrder = models.ForeignKey(ClientOrder,on_delete=models.SET_NULL,null=True,blank=True)

class ItemSupplierOrder(models.Model):
    supplierOrder = models.ForeignKey(SupplierOrder,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=80,blank=True)
    quantity = models.IntegerField(default=1)
    priceUnitary = models.IntegerField(blank=True,null=True)
    priceTotal = models.IntegerField()
    dateTop = models.IntegerField(blank=True,null=True)

class SupplierInvoice(models.Model):
    supplierOrder = models.ForeignKey(SupplierOrder,on_delete=models.CASCADE)
    data = models.JSONField(null=True,blank=True)
    dateInvoice = models.DateField()