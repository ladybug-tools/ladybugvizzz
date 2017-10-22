"""
LadybugVizz | Wind rose chart
"""


from __future__ import division
from __locateEPW import locateEPW
from ladybug.epw import EPW
x = locateEPW('Djakarta Indonesia')
# isolate the first result.
res1 = x[0]

# Get the climate data class.
weatherData = res1.climateDataClass
weatherArchive = weatherData.download()
epw = weatherData.getEpwFile()
epwObj = EPW(epw)
longitude,latitude,meridian = epwObj.location.longitude,epwObj.location.latitude,epwObj.location.timezone


import matplotlib
#matplotlib.use('Qt4Agg')

import numpy as np
import matplotlib.pyplot as plt
from getWeatherData import returnWeatherDataDict
import ladybug.sunpath as sp
import ladybug.analysisperiod as prd
import ladybug.location as lc

#Location = lc.Location(latitude=, longitude=, timezone=)


def June():
    HOY = []
    for i in range(24):
        HOY.append(prd.DateTime(6,21,i))
    return HOY

def ALTs():
    Alt = []
    for i in June():
        Alt.append(str(sp.Sunpath(latitude,0,longitude,meridian/15,None).calculateSunFromDataTime(i)))#._altitude
    return Alt

x,y,z = ALTs().replace("(x:","").replace(", y:"," ").replace(", z:"," ").replace(")","").split(" ")[5],ALTs().replace("(x:","").replace(", y:"," ").replace(", z:"," ").replace(")","").split(" ")[6],ALTs().replace("(x:","").replace(", y:"," ").replace(", z:"," ").replace(")","").split(" ")[7]

print x,y,z
#print sp.Sun(June,ALT,2,False,False,0,data=None)
#print sp.Sun(12,32,)
