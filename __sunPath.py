"""
LadybugVizz | Wind rose chart
"""
from __future__ import division
import matplotlib
matplotlib.use('Qt4Agg')

from __locateEPW import locateEPW
from ladybug.epw import EPW
x = locateEPW('Manhattan')
# isolate the first result.
res1 = x[0]

# Get the climate data class.
weatherData = res1.climateDataClass
weatherArchive = weatherData.download()
epw = weatherData.getEpwFile()
epwObj = EPW(epw)
longitude,latitude,meridian = epwObj.location.longitude,epwObj.location.latitude,epwObj.location.timezone

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from getWeatherData import returnWeatherDataDict
import ladybug.sunpath as sp
import ladybug.analysisperiod as prd


# function to get HOYs for each hour, with a variable month
def Period(month):
    HOY = []
    for i in range(0,240,10):
            HOY.append(prd.DateTime(month,21,i/10))
    return HOY


# call the HOYs from above to generate the Sunpotition by datetime from Ladybug
def ALTs(month):
    Alt = []
    for i in Period(month):
        Alt.append(str(sp.Sunpath(latitude,0,longitude,meridian/15,None).calculateSunFromDataTime(i)))
    return Alt


# create a list with from the above strings for Summer - Winter solstice, and Equinox
def allAlts():
    alts = []
    alts.append(ALTs(12))
    alts.append(ALTs(3))
    alts.append(ALTs(6))
    return alts
ALT = allAlts()


# get final list of x and y positions for the defined periods.
def Summer(month):
    sunsX = []
    sunsY = []
    for i in ALT[month]:
        x,y,z = i.replace("(x:","").replace(", y:"," ").replace(", z:"," ").replace(")","").split(" ")[5], i.replace("(x:","").replace(", y:"," ").replace(", z:"," ").replace(")","").split(" ")[6], i.replace("(x:","").replace(", y:"," ").replace(", z:"," ").replace(")","").split(" ")[7]
        if float(z) < 0:
            newX = float(x) / (1 - float(z))
            newY = float(y) / (1 - float(z))
            sunsX.append((newX)*-100)
            sunsY.append((newY)*-100)
    return sunsX,sunsY


# Build the arrays for Matplotlib
Y1 = (Summer(0)[0])
X1 = (Summer(0)[1])
Y2 = (Summer(1)[0])
X2 = (Summer(1)[1])
Y3 = (Summer(2)[0])
X3 = (Summer(2)[1])


# function to get HOYs for each Month, with a variable hour
def Period_anallem(hour):
    HOY = []
    for i in range(1,13):
            HOY.append(prd.DateTime(i,21,hour))
    HOY.append(prd.DateTime(1,21,hour))
    return HOY


# call the HOYs from above to generate the Sunpotition by datetime from Ladybug
def ALTs_anallem(hour):
    Alt = []
    for i in Period_anallem(hour):
        Alt.append(str(sp.Sunpath(latitude,0,longitude,meridian/15,None).calculateSunFromDataTime(i)))
    return Alt


# create a list with from the above strings for all hours of day
def allAlts_anallem():
    alts = []
    alts.append(ALTs_anallem(0))
    alts.append(ALTs_anallem(1))
    alts.append(ALTs_anallem(2))
    alts.append(ALTs_anallem(3))
    alts.append(ALTs_anallem(4))
    alts.append(ALTs_anallem(5))
    alts.append(ALTs_anallem(6))
    alts.append(ALTs_anallem(7))
    alts.append(ALTs_anallem(8))
    alts.append(ALTs_anallem(9))
    alts.append(ALTs_anallem(10))
    alts.append(ALTs_anallem(11))
    alts.append(ALTs_anallem(12))
    alts.append(ALTs_anallem(13))
    alts.append(ALTs_anallem(14))
    alts.append(ALTs_anallem(15))
    alts.append(ALTs_anallem(16))
    alts.append(ALTs_anallem(17))
    alts.append(ALTs_anallem(18))
    alts.append(ALTs_anallem(19))
    alts.append(ALTs_anallem(20))
    alts.append(ALTs_anallem(21))
    alts.append(ALTs_anallem(22))
    alts.append(ALTs_anallem(23))
    return alts
ALT_anallem = allAlts_anallem()


# get final list of x and y positions for the defined periods.
def Anallem(hour):
    sunsX = []
    sunsY = []
    for i in ALT_anallem[hour]:
        x,y,z = i.replace("(x:","").replace(", y:"," ").replace(", z:"," ").replace(")","").split(" ")[5], i.replace("(x:","").replace(", y:"," ").replace(", z:"," ").replace(")","").split(" ")[6], i.replace("(x:","").replace(", y:"," ").replace(", z:"," ").replace(")","").split(" ")[7]
        if float(z) < 0:
            newX = float(x) / (1 - float(z))
            newY = float(y) / (1 - float(z))
            sunsX.append((newX)*-100)
            sunsY.append((newY)*-100)
    return sunsX,sunsY


# Build the arrays for Matplotlib
Y_anallem0 = (Anallem(0)[0])
X_anallem0 = (Anallem(0)[1])
Y_anallem1 = (Anallem(1)[0])
X_anallem1 = (Anallem(1)[1])
Y_anallem2 = (Anallem(2)[0])
X_anallem2 = (Anallem(2)[1])
Y_anallem3 = (Anallem(3)[0])
X_anallem3 = (Anallem(3)[1])
Y_anallem4 = (Anallem(4)[0])
X_anallem4 = (Anallem(4)[1])
Y_anallem5 = (Anallem(5)[0])
X_anallem5 = (Anallem(5)[1])
Y_anallem6 = (Anallem(6)[0])
X_anallem6 = (Anallem(6)[1])
Y_anallem7 = (Anallem(7)[0])
X_anallem7 = (Anallem(7)[1])
Y_anallem8 = (Anallem(8)[0])
X_anallem8 = (Anallem(8)[1])
Y_anallem9 = (Anallem(9)[0])
X_anallem9 = (Anallem(9)[1])
Y_anallem10 = (Anallem(10)[0])
X_anallem10 = (Anallem(10)[1])
Y_anallem11 = (Anallem(11)[0])
X_anallem11 = (Anallem(11)[1])
Y_anallem12 = (Anallem(12)[0])
X_anallem12 = (Anallem(12)[1])
Y_anallem13 = (Anallem(13)[0])
X_anallem13 = (Anallem(13)[1])
Y_anallem14 = (Anallem(14)[0])
X_anallem14 = (Anallem(14)[1])
Y_anallem15 = (Anallem(15)[0])
X_anallem15 = (Anallem(15)[1])
Y_anallem16 = (Anallem(16)[0])
X_anallem16 = (Anallem(16)[1])
Y_anallem17 = (Anallem(17)[0])
X_anallem17 = (Anallem(17)[1])
Y_anallem18 = (Anallem(18)[0])
X_anallem18 = (Anallem(18)[1])
Y_anallem19 = (Anallem(19)[0])
X_anallem19 = (Anallem(19)[1])
Y_anallem20 = (Anallem(20)[0])
X_anallem20 = (Anallem(20)[1])
Y_anallem21 = (Anallem(21)[0])
X_anallem21 = (Anallem(21)[1])
Y_anallem22 = (Anallem(22)[0])
X_anallem22 = (Anallem(22)[1])
Y_anallem23 = (Anallem(23)[0])
X_anallem23 = (Anallem(23)[1])


# build colors arrays for sun positions
colors1 = Y1
colors2 = Y2
colors3 = Y3


# start generating the plot
fig, ax = plt.subplots()


# plot 1st graph with sun positions and curves for sunPath and anallema.
ax.scatter(Y1, X1, c=colors1, cmap='hsv', alpha=1)
ax.plot(Y1, X1, 'k-', lw=1)
ax.scatter(Y2, X2, c=colors2, cmap='hsv', alpha=1)
ax.plot(Y2, X2, 'k-', lw=1)
ax.scatter(Y3, X3, c=colors3, cmap='hsv', alpha=1)
ax.plot(Y3,X3, 'k-', lw=1)
ax.plot([0, 0], [100, -100], 'k:', lw=0.5, alpha=0.5)
ax.plot([-100,100], [0,0], 'k:', lw=0.5, alpha=0.5)
ax.plot(Y_anallem0, X_anallem0, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem1, X_anallem1, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem2, X_anallem2, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem3, X_anallem3, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem4, X_anallem4, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem5, X_anallem5, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem6, X_anallem6, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem7, X_anallem7, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem8, X_anallem8, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem9, X_anallem9, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem10, X_anallem10, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem11, X_anallem11, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem12, X_anallem12, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem13, X_anallem13, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem14, X_anallem14, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem15, X_anallem15, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem16, X_anallem16, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem17, X_anallem17, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem18, X_anallem18, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem19, X_anallem19, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem20, X_anallem20, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem21, X_anallem21, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem22, X_anallem22, 'k-', lw=0.5, alpha=0.5)
ax.plot(Y_anallem23, X_anallem23, 'k-', lw=0.5, alpha=0.5)
ax.set_xlim([-100,100])
ax.set_ylim([-100,100])
ax.set(aspect=1)
ax.axis('off')


# plot second graph for background image, hiding axes and grid.
figB, bx = plt.subplots()
bx = plt.subplot(111, projection='polar')
thetaB = np.linspace(0, 2*np.pi, 1)
r = np.sqrt(1)
bx.plot(r*np.cos(thetaB), r*np.sin(thetaB))
bx.set_theta_zero_location("N")
bx.set_theta_direction(-1)
plt.xticks(np.radians(range(0, 360, 45)),
                   ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
bx.grid(False)
bx.axes.get_yaxis().set_visible(False)


# general properties for the image saving
fig.set_size_inches(8,8)
fig.savefig('test.png',dpi=300, transparent=True)
figB.set_size_inches(8,8)
figB.savefig('background.png',dpi=300)


#plt.show()
