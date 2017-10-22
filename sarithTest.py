from getWeatherData import returnWeatherDataDict
import matplotlib
#matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt
import numpy as np
import os
from utilities.colors import colorList


x = returnWeatherDataDict("Melbourne Australia")

drybulb= tuple(float(i) for i in x["dryBulbTemperature"])


# Working example:
color = colorList.index("magma")

valList = []
counter = 0
for hour in range(24):
    newList = []
    for date in range(365):
        newList.append(drybulb[counter])


        counter+=1
    valList.append(newList)

plt.imshow(valList, interpolation = "nearest", aspect = 3, cmap = colorList[color])
plt.savefig("test/name.png")