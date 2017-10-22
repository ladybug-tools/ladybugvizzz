# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import Django libraries
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .forms import CityForm

# Import python modules
import random
import os


# Import Ladybug
rootDir = os.getcwd() + '\\vizzz\\assets\\'
print rootDir
import sys
sys.path.append(rootDir)
import ladybug
import utilities
import getWeatherData
import getWeatherPlots

# Variable to track city.
currentCity = "None"

# Dictonary of full data types.
dataDict = {"diffuseHorizontalRadiation": ("Diffuse Horizontal Radiation", 'inferno'),
            'dryBulbTemperature': ("Dry Bulb Temperature", 'magma'),
            'relativeHumidity': ("Relative Humidity", 'Blues'),
            'windSpeed': ("Wind Speed", 'Blues'),
            'globalHorizontalRadiation': ("Global Horizontal Radiation", 'Greens'),
            'directNormalRadiation': ("Direct Normal Radiation", 'inferno'),
            'diffuseHorizontalRadiation': ("Diffuse Horizontal Radiation", 'plasma'),
            'horizontalInfraredRadiationIntensity': ("Horizontal Infrared Radiation Intensity", 'plasma'),
            'globalHorizontalIlluminance': ("Global Horizontal Illuminance", 'plasma'),
            'directNormalIlluminance': ("Direct Normal Illuminance", 'Reds'),
            'diffuseHorizontalIlluminance': ("Diffuse Horizontal Illuminance", 'plasma')}

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        print "Empty form"
        form = CityForm()
        return render(request, 'index.html', {'form': form})

    @csrf_exempt
    def post(self, request, **kwargs):
        cityname = request.POST.get("city_name", default="New York")
        dataType = request.POST.get("data_type", default="dryBulbTemperature")
        legColor = request.POST.get("color", default="plasma")
        print "Submitted city: " + cityname
        form = CityForm(request.POST)

        windRosePath = os.getcwd() + '\\vizzz\\static\\windrose.png'
        windRelpath = '\\static\\windrose.png'
        heatMapPath = os.getcwd() + '\\vizzz\\static\\heatmap.png'
        heatRelpath = '\\static\\heatmap.png'

        if currentCity != cityname:
            y = getWeatherPlots.returnWeatherDataDict(locationString="Dallas Texas USA", plotGoogleMapPath='googleMap.html')
            z = getWeatherPlots.returnWindRose(y,divisions=None,filepath=windRosePath)
        a = getWeatherPlots.returnHeatMap(y,filepath=heatMapPath,dataType=dataType,dataLabel=dataDict[dataType][0], colormap=legColor)


        #cityPicUrl = getWeatherData.returnWeatherDataDict(cityname)
        return render(request, 'index.html', {'form': form, 'windPicUrl': windRelpath, 'heatPicUrl': heatRelpath})
