from django.db import models

from vet.models import Client, Personnel


class Discussion(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    interlocuteur=models.ForeignKey(Personnel,on_delete=models.CASCADE)
    debut=models.DateTimeField()
    fin=models.DateTimeField()
    etat=models.IntegerField() # 0 if not closed, 1 if closed and paid,-1 if not paid and not closed during on 24h