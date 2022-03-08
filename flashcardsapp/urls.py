from django.urls import path
from . import views

urlpatterns = [
    path("createflash-<int:id>", views.createFlash, name="createFlash"),
    path("updateflash-<int:id>", views.updateFlash, name="updateFlash"),
    path("deleteflash-<int:id>", views.deleteFlash, name="deleteFlash"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("question-<int:id>", views.question, name="question"),
    path("answer-<int:id>", views.answer, name="answer"),
    path("deck-<int:id>", views.deckview, name="deckview"),
]
