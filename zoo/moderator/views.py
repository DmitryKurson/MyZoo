from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import AnimalForm
from main.models import Animal

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


def show_moderator_main_page(request):
    return render(request, "moderator/main_page.html")

def show_animals(request):
    all_animals = Animal.objects.all()
    filtered_animals = all_animals

    if request.method == 'POST':
        filters = [request.POST.get("filter_id"), request.POST.get("filter_type"), request.POST.get("filter_color"), request.POST.get("filter_age"), request.POST.get("filter_zone")]

        filtered_animals = []
        for i in all_animals:
            animal_attr = [i.id, i.type, i.color, i.age, i.zone]
            for j in range(len(animal_attr)):
                if filters[j] != '' and filters[j] == animal_attr[j]:
                    filtered_animals.append(i)

    return render(request, "moderator/animal/show.html", {'all_animals':filtered_animals})


def animal_create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../animals")

    form = AnimalForm
    return render(request, "moderator/animal/create.html", {'form':form})



