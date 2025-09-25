from django.http import HttpResponse
import logging
from django.shortcuts import render
from .models import *

logger = logging.getLogger('main')

def show_main_page(request):
    logger.info("Користувач перейшов на головну сторінку")
    return render(request, "main/main_page.html")

def show_contacts(request):
    logger.info("Користувач перейшов на сторінку контактів")
    return render(request, "main/contacts.html")

def show_prices(request):
    logger.error("Користувач перейшов на сторінку цін")
    return render(request, "main/prices.html")

def show_about(request):
    return render(request, "main/about.html")

def show_animals(request):
    all_animals = Animal.objects.all()
    count_of_animals = len(all_animals)
    return render(request, "main/animals.html", {'animals':all_animals, "count":count_of_animals})
