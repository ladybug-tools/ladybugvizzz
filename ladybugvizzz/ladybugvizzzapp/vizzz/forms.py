from django import forms
from django.db import models


datTyps = (
        ('dryBulbTemperature', 'Dry Bulb Temperature'),
        ('dewPointTemperature', 'Dew Point Temperature'),
        ('relativeHumidity', 'Relative Humidity'),
        ('windSpeed', 'Wind Speed'),
        ('globalHorizontalRadiation', 'Global Horizontal Radiation'),
        ('directNormalRadiation', 'Direct Normal Radiation'),
        ('diffuseHorizontalRadiation', 'Diffuse Horizontal Radiation'),
        ('horizontalInfraredRadiationIntensity', 'Horizontal Infrared Radiation'),
        ('globalHorizontalIlluminance', 'Global Horizontal Illuminance'),
        ('directNormalIlluminance', 'Direct Normal Illuminance'),
        ('diffuseHorizontalIlluminance', 'Diffuse Horizontal Illuminance'),)

legColors = (
        ('plasma', 'Plasma'),
        ('inferno', 'Inferno'),
        ('magma', 'Magma'),
        ('Greys', 'Greys'),
        ('Purples', 'Purples'),
        ('Blues', 'Blues'),
        ('Greens', 'Greens'),
        ('Oranges', 'Oranges'),
        ('Reds', 'Reds'),
        ('YlOrBr', 'YellowOrangeBrown'),
        ('YlOrRd', 'OrangeRed'),
        ('PuRd', 'PurpleRed'),
        ('RdPu', 'Red Purple'),
        ('BuPu', 'BluePurple'),
        ('GnBu', 'GreenBlue'),
        ('PuBu', 'PurplBlue'),
        ('YlGnBu', 'YellowGreenBlue'),
        ('PuBuGn', 'PurpleBlueGreen'),
        ('BuGn', 'BlueGreen'),
        ('YlGn', 'YellowGreen'),)


class DatTyp(models.Model):
    datTyp = models.CharField(max_length=25,choices=datTyps)

class LegColor(models.Model):
    legColor = models.CharField(max_length=25,choices=legColors)

class CityForm(forms.Form):
    city_name = forms.CharField(label='City Name', max_length=100)
    data_type = forms.ChoiceField(label='Data Type', choices=datTyps)
    color = forms.ChoiceField(label='Color', choices=legColors)
