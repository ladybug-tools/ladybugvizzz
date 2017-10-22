# coding=utf-8
"""
The function haversine calculates the distance between two longitudes and latitudes based
on the Haversine Formula (https://en.wikipedia.org/wiki/Haversine_formula). The distance
calculated is the great-circle distance i.e. the shortest distance between two points in a
Euclidean space.


Got the function from: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
"""
from __future__ import division
from math import radians, cos, sin, asin, sqrt
import re

class LongitudeLatitude(object):

    def __init__(self,longlatString=None,longitude=None,latitude=None):
        self.longLatString=longlatString
        self.longitude=longitude
        self.latitude=latitude

    @property
    def longLatString(self):
        return self._longLatString

    @longLatString.setter
    def longLatString(self,longitudeLatitudeString):

        def remove_non_ascii_1(text, remove=128):

            return ''.join(i for i in text if ord(i) < remove)

        l = re.split('[,°\'"\s]+', longitudeLatitudeString)

        for values in l:
                values = remove_non_ascii_1(values, remove=128)

def haversine(lon1, lat1, lon2, lat2,useMiles=True):
    """
    Calculate the great circle distance between two points on the earth
    (specified in decimal degrees)
    :param lon1: Longitude of first Location
    :param lat1: Latitude of first location
    :param lon2: Longitude of second location
    :param lat2: Longitude of second location.
    :param useMiles: If set to True distance will be calculated in miles. Else it will be
        calculated in kilometers.
    :return: Distance between the two locations.
    """

    earthRadius = 3956 if useMiles else 6371

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = earthRadius

    return c * r

