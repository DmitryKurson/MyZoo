from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def show_contacts(request):
    return render(request, "main/contacts.html")

def show_prices(request):
    return render(request, "main/prices.html")

def show_about(request):
    return render(request, "main/about.html")


