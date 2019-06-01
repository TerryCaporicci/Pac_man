from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('scoreboard', views.score)
]
