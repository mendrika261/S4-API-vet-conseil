from django.db import models

from . import Client
from . import patient


class Patient(models.Model):
    age=models.IntegerField()
    proprietaire=models.ForeignKey(Client, on_delete=models.CASCADE,related_name='patients')
    
    

