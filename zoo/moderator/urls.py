from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_admin_main_page, name="admin_main_page"),
    path('animals', views.show_animals, name="animals_m"),
    path('animals/create', views.animal_create, name="animals_create")


    #path('clients', views.??, name="clients"),
    #path('clients', views.??, name="workers"),

]
