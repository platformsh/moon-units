from django.db import models

# Create your models here.


class Moon(models.Model):
    name = models.CharField(max_length=255, null=False)
    planet = models.CharField(max_length=255, null=False)
    discovered = models.DateField()
    volume = models.FloatField()


