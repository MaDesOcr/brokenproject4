from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return render(request, 'articles/home.html')

def welcome(request):
    return HttpResponse("<p>Bienvenue sur mon blog !</p>")

def current_time(request):
    now = datetime.now()
    return HttpResponse(f"<p>L'heure actuelle est : {now.strftime('%H:%M:%S')}</p>")

def greet_user(request, name):
    return render(request, 'articles/greet.html', {'name': name.capitalize()})
