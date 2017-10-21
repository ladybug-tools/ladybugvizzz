"""
=======================
Pie chart on polar axis
=======================

Demo of bar plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt


angles = [0,22.5,45,67.5,90,112.5,135,157.5,180,202.5,225,247.5,270,292.5,315,337.5,360]
maxWind = 17

def Legend():
    legend = []
    for i in range(0,maxWind*100,((maxWind*100)/10)):
        legend.append(i/100)
    return legend

print Legend()

def wind_data(dir):
    EPW = open("C:\\Users\\byron\\Documents\\GitHub\\ladybugvizzz\\temp_wind\\GBR_London.Gatwick.037760_IWEC.epw", "r")
    wind = []
    wind_byDir = []
    lines = EPW.readlines()
    for f in lines[8:]:
        EPW_split = f.split(",")
        wind.append(float(EPW_split[21]))
        if float(EPW_split[20]) >= angles[dir] and float(EPW_split[20]) < angles[dir+1]:
            wind_byDir.append(float(EPW_split[21]))
    EPW.close()
    MAX = int(float(max(wind)))
    return wind, MAX, wind_byDir

def Speed_byDir(dir):
    speed = []



def frequence():
    perce = []
    for i in range(10):
        perce.append(len(wind_data(i)[2])*100/len(wind_data(i)[0]))
    return perce, max(perce)



# Compute pie slices
N = 16
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
#radii = frequence()[1] * frequence()[0]
radii = np.array(frequence()[0])
width = np.pi / N*2 #4 * np.random.rand(N)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)

# Use custom colors and opacity
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)

plt.show()
# plt.savefig("plot.svg")
# plt.savefig("plot.png")
# plt.savefig("plot.pdf")
