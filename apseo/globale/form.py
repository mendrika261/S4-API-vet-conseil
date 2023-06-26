from django import forms
from .models import Client
from .models import Patient

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom','prenom','adresse', 'mail', 'contact'] 
        
