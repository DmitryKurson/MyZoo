import json
import os
from hashlib import sha256
from dotenv import load_dotenv

from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import AnimalForm
from main.models import Animal

load_dotenv()

class AnimalDetailView(DetailView):
    model = Animal
    template_name = "moderator/animal/detail_view.html"
    context_object_name = "animal"

class AnimalUpdateView(UpdateView):
    model = Animal
    template_name = "moderator/animal/update.html"
    form_class = AnimalForm

class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = '..'
    template_name = "moderator/animal/delete.html"

def show_moderator_login(request):
    if request.method=='POST':
        entered_login = sha256(request.POST.get("login").encode()).hexdigest()
        entered_password = sha256(request.POST.get("password").encode()).hexdigest()

        correct_login = os.getenv("MYZOO_LOGIN")
        correct_password = os.getenv("MYZOO_PASSWORD")

        if entered_login == correct_login and entered_password == correct_password:
            return redirect("main_page_m")

    return render(request, "moderator/login.html")

def show_moderator_main_page(request):
    return render(request, "moderator/main_page.html")

def show_animals(request):
    all_animals = Animal.objects.all()
    sort_field = request.GET.get("sort", "id")
    direction = request.GET.get("dir", "asc")

    if request.method == 'POST':
        filters_fields = ['id', 'type', 'color', 'age', 'zone']
        filters = {}
        for i in filters_fields:
            value = request.POST.get(f"filter_{i}")
            if value:
                filters[i] = value
        all_animals = Animal.objects.filter(**filters)

    if direction == 'desc':
        all_animals = all_animals.order_by(f"-{sort_field}")
    else:
        all_animals = all_animals.order_by(sort_field)

    return render(request, "moderator/animal/show.html", {'all_animals':all_animals, "sort_field":sort_field, "direction":direction})

def animal_create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../animals")

    form = AnimalForm
    return render(request, "moderator/animal/create.html", {'form':form})

def save_animals_to_file(request):
    animals = Animal.objects.all()
    data = {
        "animals":[
            {
                "id": animal.id,
                "type": animal.type,
                "color": animal.color,
                "age":  animal.age,
                "zone": animal.zone
            } for animal in animals
        ]
    }
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return render(request, "moderator/ok_export.html")