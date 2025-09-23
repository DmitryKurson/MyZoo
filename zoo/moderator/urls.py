from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_moderator_main_page, name="moderator_main_page"),
    path('animals/', views.show_animals, name="animals_mm"),
    path('animals', views.show_animals, name="animals_m"),
    path('animals/<int:pk>', views.AnimalDetailView.as_view(), name="detail_view"),
    path('animals/create', views.animal_create, name="animals_create"),
    path('animals/<int:pk>/update', views.AnimalUpdateView.as_view(), name="animal_update"),
    path('animals/<int:pk>/delete', views.AnimalDeleteView.as_view(), name="animal_delete" )

    #path('clients', views.??, name="clients"),
    #path('clients', views.??, name="workers"),

]
