from django.db import models

from . import Personnel

class Login(models.Model):
    personnel=models.ForeignKey(Personnel, on_delete=models.CASCADE)
    mail=models.CharField(max_length=255)
    identifiant=models.CharField(max_length=100)
    mot_de_passe=models.CharField(max_length=255)