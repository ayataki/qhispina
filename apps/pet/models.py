from __future__ import absolute_import
from django.db import models

from apps.adoption.models import Person


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.name


class Pet(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=10)
    age_aprox = models.IntegerField()
    date_in = models.DateField()
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    vaccine = models.ManyToManyField(Vaccine, blank=True)
