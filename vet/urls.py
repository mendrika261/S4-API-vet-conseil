from django.urls import path

from vet.views import rendez_vous_view


urlpatterns = [
    path("", rendez_vous_view.index, name="index"),
    path("insertion_rendez_vous", rendez_vous_view.insertion_rendez_vous, name="insertion"),
    path("<int:id_rendez_vous>/rendez_vous_by_id", rendez_vous_view.rendez_vous_by_id, name="rendez_vous_by_id"),
    path("tous_les_rendez_vous", rendez_vous_view.tous_les_rendez_vous, name="tous_les_rendez_vous"),
    path("rendez_vous_par_jour/<str:jours>/", rendez_vous_view.rendez_vous_par_jour, name="rendez_vous_par_jour"),
    path("rendez_vous_entre_deux_dates/<str:date_debut>/<str:date_fin>", rendez_vous_view.rendez_vous_entre_deux_dates, name="rendez_vous_entre_deux_dates"),
    path("supprimer_rendez_vous/<int:rendez_vous_id>", rendez_vous_view.supprimer_rendez_vous, name="supprimer_rendez_vous"),
]