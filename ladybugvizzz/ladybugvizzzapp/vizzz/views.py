# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import Django libraries
from django.shortcuts import render
from django.http import HttpResponse

# Import python modules
import random
import os


# Import Ladybug
rootDir = '\\'.join(os.getcwd().split('\\')[0:-2])
import sys
sys.path.append(rootDir)
import ladybug
import getWeatherData

# Create your views here.
def index(request):
    """"
    Return a random city from the list of cities in the csv file at __epwLocations/largeCities.csv
    :param beginsWith: Filter cities starting with these letters.
    :param endsWith:  Filter cities ending with these letters.
    :return:
    """
    cityList = []
    rootDir2 = '\\'.join(os.getcwd().split('\\')[0:-2])
    print rootDir2
    file_path = rootDir2 + '\__epwLocations\largeCities.csv'
    with open(file_path, 'r') as cityData:
        for lines in cityData:
            if lines.strip():
                cityList.append(lines.strip())

    randomCity = str(random.choice(cityList))
    cityData = getWeatherData.returnWeatherDataDict(randomCity)
    print cityData

    city = '<h1>' + randomCity + "</h1>"

    return HttpResponse(city)
