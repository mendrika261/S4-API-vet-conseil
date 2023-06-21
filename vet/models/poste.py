from django.db import models
class Poste(models.Model):
    designation = models.CharField(max_length=255)
