from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def show_main_page(request):
    return render(request, "main/main_page.html")

def show_contacts(request):
    return render(request, "main/contacts.html")

def show_prices(request):
    return render(request, "main/prices.html")

def show_about(request):
    return render(request, "main/about.html")

def show_animals(request):
    all_animals = Animal.objects.all()
    count_of_animals = len(all_animals)
    return render(request, "main/animals.html", {'animals':all_animals, "count":count_of_animals})
