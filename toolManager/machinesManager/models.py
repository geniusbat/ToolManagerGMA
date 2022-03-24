from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=20)
    workspaceLimitX = models.FloatField(null=True,blank=True)
    workspaceLimitY = models.FloatField(null=True,blank=True)
    workspaceLimitZ = models.FloatField(null=True,blank=True)
    maxSpeed = models.FloatField(null=True,blank=True)
    precision = models.FloatField(null=True,blank=True)
    data = models.JSONField(null=True,blank=True)
    def __str__(self) -> str:
        return self.name