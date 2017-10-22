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
import getWeatherData
import __windrose


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        print "Empty form"
        form = CityForm()
        return render(request, 'index.html', {'form': form})

    @csrf_exempt
    def post(self, request, **kwargs):
        cityname = request.POST.get("city_name", default="New York")
        print "Submitted city: " + cityname
        form = CityForm(request.POST)
        imgPath = os.getcwd() + '\\vizzz\\static\\windrose.png'
        windRose = __windrose.returnWindRose(imgPath, cityname)
        relpath = '\\static\\windrose.png'
        #cityPicUrl = getWeatherData.returnWeatherDataDict(cityname)
        return render(request, 'index.html', {'form': form, 'cityPicUrl': relpath})
