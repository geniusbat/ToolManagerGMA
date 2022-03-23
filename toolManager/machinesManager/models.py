from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=20)
    workspaceLimitX = models.FloatField()
    workspaceLimitY = models.FloatField()
    workspaceLimitZ = models.FloatField()
    maxSpeed = models.FloatField()
    precision = models.FloatField()
    def __str__(self) -> str:
        return self.name