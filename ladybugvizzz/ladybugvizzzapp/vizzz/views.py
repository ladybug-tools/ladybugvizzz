# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import Django libraries
from django.shortcuts import render
from django.http import HttpResponse

# Import python modules
import random
import os


# Import Ladybug

rootDir = os.getcwd()
import sys
sys.path.append(os.path.join(rootDir,'vizzz','assets'))
import ladybug
import getWeatherData
import __locateEPW
import locationCalc
import __extractEPW

# Create your views here.
def index(request):
    """"
    Return a random city from the list of cities in the csv file at __epwLocations/largeCities.csv
    :param beginsWith: Filter cities starting with these letters.
    :param endsWith:  Filter cities ending with these letters.
    :return:
    """
    cityList = []
    rootDir = os.getcwd()
    file_path = rootDir + '\\vizzz\\assets\__epwLocations\largeCities.csv'
    with open(file_path, 'r') as cityData:
        for lines in cityData:
            if lines.strip():
                cityList.append(lines.strip())

    randomCity = str(random.choice(cityList))
    cityData = getWeatherData.returnWeatherDataDict(randomCity)

    city = '<h1>' + randomCity + "</h1>"
    city = city + str(cityData)

    return HttpResponse(city)
