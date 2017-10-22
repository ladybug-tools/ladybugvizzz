"""
LadybugVizz | Wind rose chart
"""


from __future__ import division
import matplotlib
#matplotlib.use('Qt4Agg')

import numpy as np
import matplotlib.pyplot as plt
from getWeatherData import returnWeatherDataDict


def returnWindRose(filepath, locationString=None, beaufortScale = None, divisions=None, Longitude=None, Latitude=None):
    """

    :param filepath: file path to save (required)
    :param locationString:
    :param divisions:
    :param Longitude:
    :param Latitude:
    :return:
    """

    assert locationString or ((Longitude is not None) and (Latitude is not None)), "either locationString or Longitude and Latitude are required."

    # call getWeatherData and get wind-speed and direction
    windData = returnWeatherDataDict(locationString=locationString,longitude=Longitude,latitude=Latitude)
    windSpeed = windData["windSpeed"]
    windDirection = windData["windDirection"]


    # define Calm (0 m/s) to filter it out later, and max-speed to create legend
    Calm = windSpeed.count(0)
    maxWind = int(max(windSpeed))


    # define radial divisions for chart
    Divisions = divisions
    if Divisions == None:
        Divisions = 8
    else: Divisions = divisions


    # define the angle division according to the divisions
    def Angles():
        angles = []
        for i in range(0,36000, int(36000/Divisions)):
            angles.append(float(i/100))
        angles.append(360)
        return angles
    angleList = Angles()


    # define the legend division according to max wind speed available
    def legendList():
        legend = []
        for i in range(0,maxWind*100,int((maxWind*100)/10)):
            legend.append(i/100)
        return legend
    WindSpeedLegend = legendList()

    beaufort = [0.3,1.5,3.3,5.5,8.0,10.8,13.9,17.2,20.7,24.5,28.4,32.6]


    # define scale
    if beaufortScale is None or beaufortScale == False:
        legendList = WindSpeedLegend
    else: legendList = beaufort


    # def wind_data(dir):
    #     wind_byDir = []
    #     for f in range(8760):
    #         if windSpeed[f] != 0:
    #             if windDirection[f] >= Angles()[dir] and windDirection[f] < Angles()[dir+1]:
    #                 wind_byDir.append(windSpeed[f])
    #     return wind_byDir


    # filter data for angle and windspeed defined above
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
        wind_11 = []
        wind_12 = []
        if beaufortScale is None or beaufortScale == False:
            for f in range(8760):
                if windSpeed[f] != 0:
                    if windDirection[f] >= angleList[dir] and windDirection[f] < angleList[dir+1]:
                        if windSpeed[f] >= legendList[0] and windSpeed[f] < legendList[1]:
                            wind_1.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[1] and windSpeed[f] < legendList[2]:
                            wind_2.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[2] and windSpeed[f] < legendList[3]:
                            wind_3.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[3] and windSpeed[f] < legendList[4]:
                            wind_4.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[4] and windSpeed[f] < legendList[5]:
                            wind_5.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[5] and windSpeed[f] < legendList[6]:
                            wind_6.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[6] and windSpeed[f] < legendList[7]:
                            wind_7.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[7] and windSpeed[f] < legendList[8]:
                            wind_8.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[8] and windSpeed[f] < legendList[9]:
                            wind_9.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[9]:
                            wind_10.append(windSpeed[f])
            #return wind_1,wind_2,wind_3,wind_4,wind_5,wind_6,wind_7,wind_8,wind_9,wind_10
        elif beaufortScale is True:
            for f in range(8760):
                if windSpeed[f] != 0:
                    if windDirection[f] >= angleList[dir] and windDirection[f] < angleList[dir+1]:
                        if windSpeed[f] >= legendList[0] and windSpeed[f] < legendList[1]:
                            wind_1.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[1] and windSpeed[f] < legendList[2]:
                            wind_2.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[2] and windSpeed[f] < legendList[3]:
                            wind_3.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[3] and windSpeed[f] < legendList[4]:
                            wind_4.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[4] and windSpeed[f] < legendList[5]:
                            wind_5.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[5] and windSpeed[f] < legendList[6]:
                            wind_6.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[6] and windSpeed[f] < legendList[7]:
                            wind_7.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[7] and windSpeed[f] < legendList[8]:
                            wind_8.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[8] and windSpeed[f] < legendList[9]:
                            wind_9.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[9] and windSpeed[f] < legendList[10]:
                            wind_10.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[10] and windSpeed[f] < legendList[11]:
                            wind_11.append(windSpeed[f])
                        elif windSpeed[f] >= legendList[11]:
                            wind_12.append(windSpeed[f])
        return wind_1,wind_2,wind_3,wind_4,wind_5,wind_6,wind_7,wind_8,wind_9,wind_10,wind_11,wind_12


    # create lists of frequencies for each wind speed
    def frequence(test):
        perce = []
        for i in range(Divisions):
            if wind_data(i)[test] == 0:
                perce.append(0)
            else:
                perce.append(len(wind_data(i)[test])*100/(len(windSpeed)-Calm))
        return perce


    #
    N = Divisions
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)

    # create arrays for each wind speed
    if beaufortScale is not True:
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
    elif beaufortScale is True:
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
        radii10 = np.array(frequence(10))
        radii11 = np.array(frequence(11))
        #radii12 = np.array(frequence(12))

    # add the arrays in order to stack bar charts later on
    if beaufortScale is not True:
        radiiCon1 = np.add(radii0,radii1)
        radiiCon2 = np.add(radiiCon1,radii2)
        radiiCon3 = np.add(radiiCon2,radii3)
        radiiCon4 = np.add(radiiCon3,radii4)
        radiiCon5 = np.add(radiiCon4,radii5)
        radiiCon6 = np.add(radiiCon5,radii6)
        radiiCon7 = np.add(radiiCon6,radii7)
        radiiCon8 = np.add(radiiCon7,radii8)
    if beaufortScale is True:
        radiiCon1 = np.add(radii0, radii1)
        radiiCon2 = np.add(radiiCon1, radii2)
        radiiCon3 = np.add(radiiCon2, radii3)
        radiiCon4 = np.add(radiiCon3, radii4)
        radiiCon5 = np.add(radiiCon4, radii5)
        radiiCon6 = np.add(radiiCon5, radii6)
        radiiCon7 = np.add(radiiCon6, radii7)
        radiiCon8 = np.add(radiiCon7, radii8)
        radiiCon9 = np.add(radiiCon8, radii9)
        radiiCon10 = np.add(radiiCon9, radii10)
        radiiCon11 = np.add(radiiCon10, radii11)


    # set bar charts in a radial array
    width = np.pi / N*2
    ax = plt.subplot(111, projection='polar')
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)


    # create bar charts for each array
    if beaufortScale is not True:
        bars0 = ax.bar(theta, radii0, width=width, bottom=0.0, color="royalblue", label = legendList[0])
        bars1 = ax.bar(theta, radii1, width=width, bottom=radii0, color="cornflowerblue", label = legendList[1])
        bars2 = ax.bar(theta, radii2, width=width, bottom=radiiCon1, color="lightskyblue", label = legendList[2])
        bars3 = ax.bar(theta, radii3, width=width, bottom=radiiCon2, color="aquamarine", label = legendList[3])
        bars4 = ax.bar(theta, radii4, width=width, bottom=radiiCon3, color="paleturquoise", label = legendList[4])
        bars5 = ax.bar(theta, radii5, width=width, bottom=radiiCon4, color="yellow", label = legendList[5])
        bars6 = ax.bar(theta, radii6, width=width, bottom=radiiCon5, color="goldenrod", label = legendList[6])
        bars7 = ax.bar(theta, radii7, width=width, bottom=radiiCon6, color="orange", label = legendList[7])
        bars8 = ax.bar(theta, radii8, width=width, bottom=radiiCon7, color="orangered", label = legendList[8])
        bars9 = ax.bar(theta, radii9, width=width, bottom=radiiCon8, color="red", label = legendList[9])
    else:
        bars0 = ax.bar(theta, radii0, width=width, bottom=0.0, color="royalblue", label="Calm")
        bars1 = ax.bar(theta, radii1, width=width, bottom=radii0, color="cornflowerblue", label="Light Air")
        bars2 = ax.bar(theta, radii2, width=width, bottom=radiiCon1, color="lightskyblue", label="Light Breeze")
        bars3 = ax.bar(theta, radii3, width=width, bottom=radiiCon2, color="lightblue", label="Gentle Breeze")
        bars4 = ax.bar(theta, radii4, width=width, bottom=radiiCon3, color="thistle", label="Moderate Breeze")
        bars5 = ax.bar(theta, radii5, width=width, bottom=radiiCon4, color="peachpuff", label="Fresh Breeze")
        bars6 = ax.bar(theta, radii6, width=width, bottom=radiiCon5, color="salmon", label="Strong Breeze")
        bars7 = ax.bar(theta, radii7, width=width, bottom=radiiCon6, color="tomato", label="High Wind")
        bars8 = ax.bar(theta, radii8, width=width, bottom=radiiCon7, color="orangered", label="Fresh Gale")
        bars9 = ax.bar(theta, radii9, width=width, bottom=radiiCon8, color="red", label="Strong Gale")
        bars10 = ax.bar(theta, radii10, width=width, bottom=radiiCon9, color="firebrick", label = "Violent Storm")
        bars11 = ax.bar(theta, radii11, width=width, bottom=radiiCon10, color="brown", label="Hurricane")
        #bars12 = ax.bar(theta, radii12, width=width, bottom=radiiCon11, color="maroon", label=legendList[12])

    plt.xticks(np.radians(range(0, 360, 45)),
                   ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])

    # set size of chart by max frequency
    plt.rgrids(range(1, int(np.amax(radiiCon8)*1.2), int(np.ceil(np.amax(radiiCon8)/5))), angle=290)

    # set legend location and title
    if beaufortScale is not True:
        plt.legend(bbox_to_anchor=(1.05,1), loc=2, title=("Wind Speed [m/s]"), frameon=False)
    else:
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title=("Beaufort Scale"), frameon=False)
    plt.title("Wind Rose")


    # for r, bar in zip(radii0, bars0):
    #     bar.set_facecolor(plt.cm.plasma(r / 10.))
    #     bar.set_alpha(0.5)



    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(8,5)
    fig.savefig(filepath, dpi=300)
    return filepath

if __name__ == "__main__":
    windRose = returnWindRose(filepath="windrose.png",locationString="New York" ,beaufortScale=True ,divisions=16)