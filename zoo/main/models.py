from ast import increment_lineno

from django.db import models

class Animal(models.Model):
    id = models.IntegerField("№", primary_key=True)
    type = models.CharField("Вид", max_length=20)
    color = models.CharField("Колір", max_length=20)
    age = models.IntegerField("Вік")
    zone = models.IntegerField("Зона")

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return f'moderator/animal/{self.id}'

class Client(models.Model):
    id = models.IntegerField("№", primary_key=True)
    name = models.CharField("Ім'я", max_length=20)
    surname = models.CharField("Прізвище", max_length=20)
    age = models.IntegerField("Вік")
    registration_date = models.DateField("Дата реєстрації")

    def __str__(self):
        return " ".join([self.name, self.surname])

class Worker(models.Model):
    id = models.IntegerField("№", primary_key=True)
    name = models.CharField("Ім'я", max_length=20)
    surname = models.CharField("Прізвище", max_length=20)
    age = models.IntegerField("Вік")
    address = models.CharField("Адреса", max_length=100)

    def __str__(self):
        return " ".join([self.name, self.surname])