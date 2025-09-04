from django.http import HttpResponse
from django.shortcuts import render

def show_main_page(request):
    return render(request, "main/main_page.html")

def show_contacts(request):
    return render(request, "main/contacts.html")

def show_prices(request):
    return render(request, "main/prices.html")

def show_about(request):
    return render(request, "main/about.html")


