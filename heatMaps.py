from getWeatherData import returnWeatherDataDict
import matplotlib
matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

"""
    At present the following outputs are supported: dryBulbTemperature, dewPointTemperature, relativeHumidity, windSpeed,
    windDirection, globalHorizontalRadiation,directNormalRadiation,diffuseHorizontalRadiation,
    horizontalInfraredRadiationIntensity,globalHorizontalIlluminance,directNormalIlluminance, diffuseHorizontalIlluminance"""

dataDict = {"diffuseHorizontalRadiation":("Diffuse Horizontal Radiation",'inferno'),
            'dryBulbTemperature':("Dry Bulb Temperature",'magma'),
            'relativeHumidity':("Relative Humidity",'Blues'),
            'globalHorizontalRadiation':("Global Horizontal Radiation",'Greens'),
            'directNormalRadiation':("Direct Normal Radiation",'inferno'),
            'diffuseHorizontalRadiation':("Diffuse Horizontal Radiation",'plasma'),
            'horizontalInfraredRadiationIntensity':("Horizontal Infrared Radiation Intensity",'plasma'),
            'globalHorizontalIlluminance':("Global Horizontal Illuminance",'plasma'),
            'directNormalIlluminance':("Direct Normal Illuminance",'Reds'),
            'diffuseHorizontalIlluminance':("Diffuse Horizontal Illuminance",'plasma')}

x = returnWeatherDataDict("Timbuktu Africa")

for dataType,values in dataDict.items():

    dataSet= tuple(float(i) for i in x[dataType])

    valList = []
    counter = 0
    for hour in range(365):
        newList = []
        for date in range(24):
            newList.append(dataSet[counter])
            counter+=1
        valList.append(newList)
    y = np.transpose(valList)
    plt.imshow(y, interpolation = "nearest", aspect = 4, cmap = values[1])
    plt.colorbar(orientation='horizontal')
    plt.title(values[0])
    plt.xlabel('Days')
    plt.ylabel('Hours')
    plt.savefig("test/%s.png"%dataType)
    plt.clf()
