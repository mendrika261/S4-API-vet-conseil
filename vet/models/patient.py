from django.db import models

from vet.models.client import Client
from vet.models.race import Race

class Patient(models.Model):
    nature=models.ForeignKey(Race, on_delete=models.CASCADE)
    age=models.IntegerField()
    proprietaire=models.ForeignKey(Client, on_delete=models.CASCADE)