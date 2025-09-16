from django.shortcuts import render, redirect

from .forms import AnimalForm

def show_admin_main_page(request):
    return render(request, "moderator/main_page.html")

def animal_create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("..")

    form = AnimalForm
    return render(request, "moderator/animal/create.html", {'form':form})



