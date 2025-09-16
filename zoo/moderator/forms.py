from django.forms import ModelForm, NumberInput, TextInput

from main.models import Animal


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ["id", "type", "color", "age", "zone"]
        widgets = {
            "id":NumberInput(attrs={
                'class': 'form-control',
                'placeholder':'Номер'
            }),
            "type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вид'
            }),
            "color": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Колір'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вік'
            }),
            "zone": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Локація'
            }),
        }



 # id = models.IntegerField("№", primary_key=True)
 #    type = models.CharField("Вид", max_length=20)
 #    color = models.CharField("Колір", max_length=20)
 #    age = models.IntegerField("Вік")
 #    zone = models.IntegerField("Зона")
