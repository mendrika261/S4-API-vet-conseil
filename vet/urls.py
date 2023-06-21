from django.urls import path

from . import views

urlpatterns = [
    #ce premier path va referencier l'url mysite/ à la vue nommée index
    path("", views.index, name="index"),
]