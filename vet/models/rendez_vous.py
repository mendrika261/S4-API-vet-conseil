from django.db import models

from vet.models import Patient

from django.shortcuts import get_object_or_404

from datetime import datetime

class Rendez_vous(models.Model):
    
    date_de_prise=models.DateTimeField() #ito tokony debut rendez vous
    date_consultation=models.DateTimeField() #ito tokony fin anle rendez-vous
    raison=models.CharField(max_length=255)
    temps=models.IntegerField()
    prix=models.FloatField()
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    etat=models.IntegerField(default=0)
    
    def rendez_vous_entre_deux_dates(self, date_debut, date_fin):
        date_debut = datetime.strptime(date_debut, "%Y-%m-%d").date()
        date_fin = datetime.strptime(date_fin, "%Y-%m-%d").date()
        liste_rendez_vous = Rendez_vous.objects.filter(date_de_prise__date__range=(date_debut, date_fin))
        return liste_rendez_vous
    
    def tous_les_rendez_vous(self):
        liste_rendez_vous = Rendez_vous.objects.all()
        return liste_rendez_vous
    
    def rendez_vous_par_jour(self, jours):
        date_jour = datetime.strptime(jours, "%Y-%m-%d").date()
        liste_rendez_vous = Rendez_vous.objects.filter(date_de_prise__date=date_jour)
        return liste_rendez_vous
    
    def rendez_vous_by_id(self):
        return get_object_or_404(self, id=self.id)
    
    def supprimer_rendez_vous(self):
        self = get_object_or_404(Rendez_vous, id=self.id)
        self.delete()
        
    def check_date(self):
        liste_rendez_vous = Rendez_vous.objects.all()
        for rendez_vous in liste_rendez_vous:
            a = rendez_vous.date_de_prise
            b = rendez_vous.date_consultation
            a2 = self.date_de_prise
            b2 = self.date_consultation
            if a < a2 and b2 > b:
                raise RuntimeError("La date est déjà prise.")
            if a > a2 and b2 < b:
                raise RuntimeError("La date est déjà prise.")
            if a > a2 and a2 < b:
                raise RuntimeError("La date est déjà prise.")
            if a > b2 and b2 < b:
                raise RuntimeError("La date est déjà prise.")
        