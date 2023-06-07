from django.db import models

from hebergement.models import Patient
from hebergement.models.nourriture import Nourriture
from hebergement.models.reservation import Reservation


class Details_reservation(models.Model):
    reservation=models.ForeignKey(Reservation,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    nourriture=models.ForeignKey(Nourriture,on_delete=models.CASCADE)
    frequence=models.IntegerField()
    medicaments=models.BooleanField()