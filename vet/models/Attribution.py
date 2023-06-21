from django.db import models

from vet.models import Race
from vet.models.nourriture import Nourriture


class Attribution(models.Model):
    nourriture=models.ForeignKey(Nourriture,on_delete=models.CASCADE)
    id_race=models.ForeignKey(Race,on_delete=models.CASCADE)
    poids_debut=models.IntegerField()
    age_debut=models.IntegerField()
    age_fin=models.IntegerField()