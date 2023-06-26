from contextlib import _RedirectStream
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

from globale.models import Race
from globale.models import Client,Patient
from .form import ClientForm
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def test(request):
    return render(request, 'index.html', {})
# insert_race
def form_insert_race(request):
    return render(request,'insert_race.html',{})

def save_race(request):
    context = {
        'saved': 'vita',
    }
    race=Race(designation=request.POST['designation'])
    race.save()
    return render(request, 'insert_race.html', context)
# list_race
def select_race(request):
    races = Race.objects.all()
    context = {'races': races}
    return render(request, 'list_race.html', context) 
# isert_client
def form_insert_client(request):
    return render(request,'insert_client.html',{})

def save_client(request):
    context = {
        'saved': 'vita',
    }
    client=Client(nom=request.POST['nom'],prenom=request.POST['prenom'],adresse=request.POST['adresse'],mail=request.POST['mail'],contact=request.POST['contact'])
    client.save()
    return render(request, 'insert_client.html', context)
# list_client
def select_client(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'list_client.html', context)
# getId_client
def client_detail(request, id_client):
    client = Client.objects.get(id=id_client)
    
    return render(request, 'client_detail.html', {'client': client})
# update_client
def update_client(request, id_client):
    client = get_object_or_404(Client, id=id_client)
    
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('client_detail', args=[id_client]))
    else:
        form = ClientForm(instance=client)
    
    return render(request, 'update_client.html', {'form': form, 'client': client})
# delet_client
def delet_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('select_client')
    
    return render(request, 'delet_client.html', {'client': client})
# insert_patient
def form_insert_patient(request):
    return render(request,'insert_patient.html',{})

def liste_clients(request):
    clients = Client.objects.values_list('id', 'nom', 'prenom')
    return render(request, 'insert_patient.html', {'clients': clients})
def save_patient(request):
    age = request.POST.get('age')
    client_id = request.POST.get('client')
    patient = Patient(age=age, proprietaire_id =client_id)
    patient.save()
    return render(request,'insert_patient.html',{})
    
# list_patient
def select_patient(request):
    patients = Patient.objects.select_related('proprietaire').all()
    return render(request, 'list_patient.html', {'patients': patients})
# delet_patient
def delet_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if request.method == 'POST':
        patient.delete()
        return redirect('select_patient')
    
    return render(request, 'delet_client.html', {'patient': patient})