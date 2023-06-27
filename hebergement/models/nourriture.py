from django.db import models


class Nourriture(models.Model):
    designation = models.CharField(max_length=255)
    prix_journalier = models.FloatField()
