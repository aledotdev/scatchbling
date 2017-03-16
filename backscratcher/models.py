from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Size(models.Model):
    name = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name


class Backscratcher(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    size = models.ManyToManyField(Size)
    price = models.FloatField()

    def __str__(self):
        return self.name
