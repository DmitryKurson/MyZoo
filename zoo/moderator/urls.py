from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_admin_main_page, name="admin_main_page"),
    path('create', views.animal_create, name="create")
]
