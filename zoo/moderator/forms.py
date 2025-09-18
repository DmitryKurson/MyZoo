from django.forms import ModelForm, NumberInput, TextInput

from main.models import Animal


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ["type", "color", "age", "zone"]
        widgets = {
            "type": TextInput(attrs={
                'class': 'form-control'
            }),
            "color": TextInput(attrs={
                'class': 'form-control'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control'
            }),
            "zone": NumberInput(attrs={
                'class': 'form-control'
            }),
        }



 # id = models.IntegerField("№", primary_key=True)
 #    type = models.CharField("Вид", max_length=20)
 #    color = models.CharField("Колір", max_length=20)
 #    age = models.IntegerField("Вік")
 #    zone = models.IntegerField("Зона")
