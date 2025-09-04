from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contacts', views.show_contacts),
    path('about', views.show_about),
    path('prices', views.show_prices)



]
