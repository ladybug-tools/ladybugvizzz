"""
=======================
Pie chart on polar axis
=======================

Demo of bar plot on a polar axis.
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from getWeatherData import returnWeatherDataDict


windData = returnWeatherDataDict(locationString="Athens Greece")#,longitude=-73.97,latitude=40.78)
windSpeed = windData["windSpeed"]
windDirection = windData["windDirection"]

Calm = windSpeed.count(0)

Divisions = 8

def Angles():
    angles = []
    for i in range(0,36000, int(36000/Divisions)):
        angles.append(float(i/100))
    angles.append(360)
    return angles

maxWind = int(max(windSpeed))

def Legend():
    legend = []
    for i in range(0,maxWind*100,int((maxWind*100)/10)):
        legend.append(i/100)
    return legend


# def wind_data(dir):
#     wind_byDir = []
#     for f in range(8760):
#         if windSpeed[f] != 0:
#             if windDirection[f] >= Angles()[dir] and windDirection[f] < Angles()[dir+1]:
#                 wind_byDir.append(windSpeed[f])
#     return wind_byDir

def wind_data(dir):
    wind_1 = []
    wind_2 = []
    wind_3 = []
    wind_4 = []
    wind_5 = []
    wind_6 = []
    wind_7 = []
    wind_8 = []
    wind_9 = []
    wind_10 = []
    for f in range(8760):
        if windSpeed[f] != 0:
            if windDirection[f] >= Angles()[dir] and windDirection[f] < Angles()[dir+1]:
                if windSpeed[f] >= Legend()[0] and windSpeed[f] < Legend()[1]:
                    wind_1.append(windSpeed[f])
                elif windSpeed[f] >= Legend()[1] and windSpeed[f] < Legend()[2]:
                    wind_2.append(windSpeed[f])
                elif windSpeed[f] >= Legend()[2] and windSpeed[f] < Legend()[3]:
                    wind_3.append(windSpeed[f])
                elif windSpeed[f] >= Legend()[3] and windSpeed[f] < Legend()[4]:
                    wind_4.append(windSpeed[f])
                elif windSpeed[f] >= Legend()[4] and windSpeed[f] < Legend()[5]:
                    wind_5.append(windSpeed[f])
                elif windSpeed[f] >= Legend()[5] and windSpeed[f] < Legend()[6]:
                    wind_6.append(windSpeed[f])
                elif windSpeed[f] >= Legend()[6] and windSpeed[f] < Legend()[7]:
                    wind_7.append(windSpeed[f])
                elif windSpeed[f] >= Legend()[7] and windSpeed[f] < Legend()[8]:
                    wind_8.append(windSpeed[f])
                elif windSpeed[f] >= Legend()[8] and windSpeed[f] < Legend()[9]:
                    wind_9.append(windSpeed[f])
                elif windSpeed[f] >= Legend()[9]:
                    wind_10.append(windSpeed[f])
    return wind_1,wind_2,wind_3,wind_4,wind_5,wind_6,wind_7,wind_8,wind_9,wind_10

def frequence(test):
    perce = []
    for i in range(Divisions):
        #for l in range(test):
        if wind_data(i)[test] == 0:
            perce.append(0)
        else:
            perce.append(len(wind_data(i)[test])*100/(len(windSpeed)-Calm))
    return perce#, max(perce)



# Compute pie slices
N = Divisions
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii0 = np.array(frequence(0))
radii1 = np.array(frequence(1))
radii2 = np.array(frequence(2))
radii3 = np.array(frequence(3))
radii4 = np.array(frequence(4))
radii5 = np.array(frequence(5))
radii6 = np.array(frequence(6))
radii7 = np.array(frequence(7))
radii8 = np.array(frequence(8))
radii9 = np.array(frequence(9))


#radii=radii.reshape(-1,10)
width = np.pi / N*2


ax = plt.subplot(111, projection='polar')
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

#ax.set_theta
bars0 = ax.bar(theta, radii0, width=width, bottom=0.0)
bars1 = ax.bar(theta, radii1, width=width, bottom=radii0)
bars2 = ax.bar(theta, radii2, width=width, bottom=radii1)
bars3 = ax.bar(theta, radii3, width=width, bottom=radii2)
bars4 = ax.bar(theta, radii4, width=width, bottom=radii3)
bars5 = ax.bar(theta, radii5, width=width, bottom=radii4)
bars6 = ax.bar(theta, radii6, width=width, bottom=radii5)
bars7 = ax.bar(theta, radii7, width=width, bottom=radii6)
bars8 = ax.bar(theta, radii8, width=width, bottom=radii7)
bars9 = ax.bar(theta, radii9, width=width, bottom=radii8)
plt.xticks(np.radians(range(0, 360, 45)),
               ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
#plt.rgrids(range(1, 20, int(np.ceil(np.amax(radii0)/5))), angle=290)
#plt.rgrids(range(1, int(np.amax(radii0)*1.2), int(np.ceil(np.amax(radii0)/5))), angle=290)

# Use custom colors and opacity
for r, bar in zip(radii0, bars0):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)

plt.show()
# plt.savefig("plot.svg")
# plt.savefig("plot.png")
# plt.savefig("plot.pdf")
