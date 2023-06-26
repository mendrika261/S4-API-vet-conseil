from django.db import models

from . import Poste


class Personnel (models.Model):
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)
    adresse=models.CharField(max_length=255)
    contact=models.CharField(max_length=255)
    poste=models.ForeignKey(Poste, on_delete=models.CASCADE)