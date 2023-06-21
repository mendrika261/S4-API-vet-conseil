from vet.models import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import vet.models.tools
import json
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    return render(request, "index.html")
#inseriont de rendez-vous
def insertion_rendez_vous(request):
    date_de_prise = request.POST.get('debut')
    date_consulation = request.POST.get('fin')
    raison = request.POST.get('raison')
    prix = 0
    idpatient = request.POST.get('idpatient')

    patient = get_object_or_404(Patient, pk=idpatient)
   
    rendez_vous = Rendez_vous(date_de_prise=date_de_prise, date_consulation=date_consulation, raison=raison, prix=prix, patient=patient)
    rendez_vous.check_date()
    rendez_vous.save()

def supprimer_rendez_vous(request, rendez_vous_id):
    rendez_vous = Rendez_vous()
    rendez_vous.id = rendez_vous_id
    rendez_vous.supprimer_rendez_vous()

#obtient rendez-vous par l'id
def rendez_vous_by_id(request, id_rendez_vous):
    rendez_vous = Rendez_vous()
    rendez_vous.id = id_rendez_vous
    rendez_vous = rendez_vous.rendez_vous_by_id()
    data = vet.models.tools.object_to_json(rendez_vous)
    return JsonResponse(data)

#les rendez vous dans une journée
def rendez_vous_par_jour(request, jours):
    date_jour = datetime.strptime(jours, "%Y-%m-%d").date()
    rendez_vous = Rendez_vous()
    liste_rendez_vous = rendez_vous.rendez_vous_par_jour(jours)#Rendez_vous.objects.filter(date_de_prise__date=date_jour)
    liste_rendez_vous_json = json.dumps(list(liste_rendez_vous.values()), cls=DjangoJSONEncoder)
    return JsonResponse(liste_rendez_vous_json, safe=False, content_type='application/json')

#tous les rendez-vous
@api_view(['GET'])
def tous_les_rendez_vous(request):
    rendez_vous = Rendez_vous()
    liste_rendez_vous = rendez_vous.tous_les_rendez_vous()
    json_object = vet.models.tools.array_object_to_json(liste_rendez_vous)
    return JsonResponse(json_object, safe=False, content_type='application/json')

#rendez vous entre deux dates
def rendez_vous_entre_deux_dates(request, date_debut, date_fin):
    rendez_vous = Rendez_vous()
    liste_rendez_vous = rendez_vous.rendez_vous_entre_deux_dates(date_debut, date_fin)#Rendez_vous.objects.filter(date_de_prise__date__range=(date_debut, date_fin))
    json_object = vet.models.tools.array_object_to_json(liste_rendez_vous)
    return JsonResponse(json_object, safe=False, content_type='application/json')