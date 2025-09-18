from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import AnimalForm
from main.models import Animal

class AnimalDetailView(DetailView):
    model = Animal
    template_name = "moderator/animal/detail_view.html"
    context_object_name = "animal"



def show_moderator_main_page(request):
    return render(request, "moderator/main_page.html")

def show_animals(request):
    all_animals = Animal.objects.all()
    return render(request, "moderator/animal/show.html", {'all_animals':all_animals})


def animal_create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("..")

    form = AnimalForm
    return render(request, "moderator/animal/create.html", {'form':form})



