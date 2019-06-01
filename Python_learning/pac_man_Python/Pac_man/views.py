from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'Pac_man/index.html')

def score(request):
    return render(request, 'Scoreboard/scoreboard.html')
