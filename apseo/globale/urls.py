"""
URL configuration for entreprise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import redirect
from django.urls import path
from globale.views import test,form_insert_race,save_race,form_insert_client,save_client,select_client,client_detail,update_client,delet_client,select_race,form_insert_patient,liste_clients,save_patient,select_patient,delet_patient


urlpatterns = [
    path('test',test, name='index'),
    path('form_insert_race',form_insert_race, name='form_insert_race'),
    path('save_race',save_race, name='save_race'),
    path('select_race',select_race, name='select_race'),
    path('form_insert_client',form_insert_client, name='form_insert_client'),
    path('save_client',save_client, name='save_client'),
    path('select_client',select_client, name='select_client'),
    path('client/<int:id_client>/',client_detail, name='client_detail'),
    path('client/<int:id_client>/update/', update_client, name='update_client'),
    path('client/<int:client_id>/delet/',delet_client, name='delet_client'),
    path('form_insert_patient',form_insert_patient, name='form_insert_patient'),
    path('liste_clients', liste_clients, name='liste_clients'),
    path('save_patient',save_patient,name='save_patient'),
    path('select_patient',select_patient, name='select_patient'),
    path('patient/<int:patient_id>/delet/',delet_patient, name='delet_patient'),
]
