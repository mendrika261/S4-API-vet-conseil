from django.db import models

from hebergement.models import Race


class Animal_accepte(models.Model):
    race=models.ForeignKey(Race,on_delete=models.CASCADE)
    debut_interval_age=models.IntegerField()
    fin_interval_age=models.IntegerField()
    debut_interval_validite=models.DateField()
    fin_interval_validite=models.DateField()
