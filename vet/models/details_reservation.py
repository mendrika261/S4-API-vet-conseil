from django.db import models

from vet.models import Patient
from vet.models.nourriture import Nourriture
from vet.models.reservation import Reservation


class Details_reservation(models.Model):
    reservation=models.ForeignKey(Reservation,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    nourriture=models.ForeignKey(Nourriture,on_delete=models.CASCADE)
    frequence=models.IntegerField()
    medicaments=models.BooleanField()