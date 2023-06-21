from django.db import models

from vet.models import Patient


class Rendez_vous(models.Model):
    date_de_prise=models.DateTimeField()
    date_consultation=models.DateTimeField()
    raison=models.CharField(max_length=255)
    temps=models.IntegerField()
    prix=models.FloatField()
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    etat=models.IntegerField(default=0)


