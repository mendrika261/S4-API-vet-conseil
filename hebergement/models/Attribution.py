from django.db import models

from hebergement.models import Race
from hebergement.models.nourriture import Nourriture


class Attribution(models.Model):
    nourriture=models.ForeignKey(Nourriture,on_delete=models.CASCADE)
    race=models.ForeignKey(Race,on_delete=models.CASCADE)
    debut_interval_poids=models.IntegerField()
    fin_interval_poids=models.IntegerField()