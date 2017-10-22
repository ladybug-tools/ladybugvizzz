from django import forms
from django.db import models

# Create your models here.
marcas = (
        ('chevrolet', 'Chevrolet'),
        ('mazda', 'Mazda'),
        ('nissan', 'Nissan'),
        ('toyota', 'Toyota'),
        ('mitsubishi', 'Mitsubishi'),)

class Marca(models.Model):
    marca = models.CharField(max_length=25,choices=marcas)

class CityForm(forms.Form):
    city_name = forms.CharField(label='City Name', max_length=100)
    data_type = forms.ChoiceField(label='Data Type', choices=marcas)
