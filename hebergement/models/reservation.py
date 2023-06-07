from django.db import models

from hebergement.models import Client


class Reservation(models.Model): 
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    date_de_prise=models.DateTimeField()
    date_debut=models.DateField()
    date_fin=models.DateField()
    prix=models.FloatField()
    etat=models.IntegerField()# 0 if still waiting for acceptation, 1 if accepted, -1 if denied
