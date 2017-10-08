from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Municipality(models.Model):
    name = models.TextField(max_length=200)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    directions = models.TextField(max_length=200, null=True)


class MunicipalityUser(User):
    municipality = models.ForeignKey('Municipality')
