# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


import random

# Create your views here.
def index(request):
    """"
    Return a random city from the list of cities in the csv file at __epwLocations/largeCities.csv
    :param beginsWith: Filter cities starting with these letters.
    :param endsWith:  Filter cities ending with these letters.
    :return:
    """
    cityList = []

    file_path = 'C:\projects\hello\helloapp\howdy\__epwLocations\largeCities.csv'
    with open(file_path, 'r') as cityData:
        for lines in cityData:
            if lines.strip():
                cityList.append(lines.strip())

    city = '<h1>' + str(random.choice(cityList)) + "</h1>"

    return HttpResponse(city)
