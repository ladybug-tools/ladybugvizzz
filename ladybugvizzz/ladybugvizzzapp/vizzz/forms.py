from django import forms

class CityForm(forms.Form):
    city_name = forms.CharField(label='City Name', max_length=100)
