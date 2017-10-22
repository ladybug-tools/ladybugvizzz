
from __future__ import division

import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from getWeatherData import returnWeatherDataDict
import ladybug.sunpath as sp
import ladybug.analysisperiod as prd

def returnWindRose(weatherDataDict,divisions=None,filepath='windrose.png'):
    """

    :param filepath: file path to save (required)
    :param locationString:
    :param divisions:
    :param Longitude:
    :param Latitude:
    :return:
    """



    # call getWeatherData and get wind-speed and direction
    windSpeed = weatherDataDict["windSpeed"]
    windDirection = weatherDataDict["windDirection"]
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
    legendList = legendList()


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
        return wind_1,wind_2,wind_3,wind_4,wind_5,wind_6,wind_7,wind_8,wind_9,wind_10


    # create lists of frequencies for each wind speed
    def frequence(test):
        perce = []
        for i in range(Divisions):
            #for l in range(test):
            if wind_data(i)[test] == 0:
                perce.append(0)
            else:
                perce.append(len(wind_data(i)[test])*100/(len(windSpeed)-Calm))
        return perce


    #
    N = Divisions
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)

    # create arrays for each wind speed
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

    # add the arrays in order to stack bar charts later on
    radiiCon1 = np.add(radii0,radii1)
    radiiCon2 = np.add(radiiCon1,radii2)
    radiiCon3 = np.add(radiiCon2,radii3)
    radiiCon4 = np.add(radiiCon3,radii4)
    radiiCon5 = np.add(radiiCon4,radii5)
    radiiCon6 = np.add(radiiCon5,radii6)
    radiiCon7 = np.add(radiiCon6,radii7)
    radiiCon8 = np.add(radiiCon7,radii8)


    # set bar charts in a radial array
    width = np.pi / N*2
    ax = plt.subplot(111, projection='polar')
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)


    # create bar charts for each array
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
    plt.xticks(np.radians(range(0, 360, 45)),
                   ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])

    # set size of chart by max frequency
    plt.rgrids(range(1, int(np.amax(radiiCon8)*1.2), int(np.ceil(np.amax(radiiCon8)/5))), angle=290)

    # set legend location and title
    plt.legend(bbox_to_anchor=(1.05,1), loc=2, title=("Wind Speed [m/s]"), frameon=False)
    plt.title("Wind Rose")


    # for r, bar in zip(radii0, bars0):
    #     bar.set_facecolor(plt.cm.plasma(r / 10.))
    #     bar.set_alpha(0.5)



    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(8,5)
    fig.savefig(filepath, dpi=300)
    plt.clf()
    return filepath

def returnHeatMap(weatherDataDict,dataType,dataLabel,colormap='plasma',filepathExtension='png',
                  ):

    filepath=dataType+"."+filepathExtension
    dataSet= tuple(float(i) for i in weatherDataDict[dataType])

    valList = []
    counter = 0
    for hour in range(365):
        newList = []
        for date in range(24):
            newList.append(dataSet[counter])
            counter+=1
        valList.append(newList)
    y = np.transpose(valList)
    plt.imshow(y, interpolation = "nearest", aspect = 4, cmap = colormap)
    plt.colorbar(orientation='horizontal')
    plt.title(dataLabel)
    plt.xlabel('Days')
    plt.ylabel('Hours')
    plt.savefig("%s"%filepath)
    plt.clf()
    return "%s"%filepath
def returnSunPath(weatherDataDict,colormap='plasma',filepath='sunpath.png',backgroundPath='background.png'):
    longitude, latitude, meridian = weatherDataDict['longitude'],weatherDataDict['latitude'],weatherDataDict['meridian']

    # function to get HOYs for each hour, with a variable month
    def Period(month):
        HOY = []
        for i in range(0, 240, 10):
            HOY.append(prd.DateTime(month, 21, i / 10))
        return HOY

    # call the HOYs from above to generate the Sunpotition by datetime from Ladybug
    def ALTs(month):
        Alt = []
        for i in Period(month):
            Alt.append(str(sp.Sunpath(latitude, 0, longitude, meridian / 15, None).calculateSunFromDataTime(i)))
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
            x, y, z = i.replace("(x:", "").replace(", y:", " ").replace(", z:", " ").replace(")", "").split(" ")[5], \
                      i.replace("(x:", "").replace(", y:", " ").replace(", z:", " ").replace(")", "").split(" ")[6], \
                      i.replace("(x:", "").replace(", y:", " ").replace(", z:", " ").replace(")", "").split(" ")[7]
            if float(z) < 0:
                newX = float(x) / (1 - float(z))
                newY = float(y) / (1 - float(z))
                sunsX.append((newX) * -100)
                sunsY.append((newY) * -100)
        return sunsX, sunsY

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
        for i in range(1, 13):
            HOY.append(prd.DateTime(i, 21, hour))
        HOY.append(prd.DateTime(1, 21, hour))
        return HOY

    # call the HOYs from above to generate the Sunpotition by datetime from Ladybug
    def ALTs_anallem(hour):
        Alt = []
        for i in Period_anallem(hour):
            Alt.append(str(sp.Sunpath(latitude, 0, longitude, meridian / 15, None).calculateSunFromDataTime(i)))
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
            x, y, z = i.replace("(x:", "").replace(", y:", " ").replace(", z:", " ").replace(")", "").split(" ")[5], \
                      i.replace("(x:", "").replace(", y:", " ").replace(", z:", " ").replace(")", "").split(" ")[6], \
                      i.replace("(x:", "").replace(", y:", " ").replace(", z:", " ").replace(")", "").split(" ")[7]
            if float(z) < 0:
                newX = float(x) / (1 - float(z))
                newY = float(y) / (1 - float(z))
                sunsX.append((newX) * -100)
                sunsY.append((newY) * -100)
        return sunsX, sunsY

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
    ax.scatter(Y1, X1, c=colors1, cmap=colormap, alpha=1)
    ax.plot(Y1, X1, 'k-', lw=1)
    ax.scatter(Y2, X2, c=colors2, cmap=colormap, alpha=1)
    ax.plot(Y2, X2, 'k-', lw=1)
    ax.scatter(Y3, X3, c=colors3, cmap=colormap, alpha=1)
    ax.plot(Y3, X3, 'k-', lw=1)
    ax.plot([0, 0], [100, -100], 'k:', lw=0.5, alpha=0.5)
    ax.plot([-100, 100], [0, 0], 'k:', lw=0.5, alpha=0.5)
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
    ax.set_xlim([-100, 100])
    ax.set_ylim([-100, 100])
    ax.set(aspect=1)
    ax.axis('off')

    # plot second graph for background image, hiding axes and grid.
    figB, bx = plt.subplots()
    bx = plt.subplot(111, projection='polar')
    thetaB = np.linspace(0, 2 * np.pi, 1)
    r = np.sqrt(1)
    bx.plot(r * np.cos(thetaB), r * np.sin(thetaB))
    bx.set_theta_zero_location("N")
    bx.set_theta_direction(-1)
    plt.xticks(np.radians(range(0, 360, 45)),
               ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
    bx.grid(False)
    bx.axes.get_yaxis().set_visible(False)

    # general properties for the image saving

    fig.set_size_inches(8, 8)
    fig.savefig(filepath, dpi=300, transparent=True)
    figB.set_size_inches(8, 8)
    figB.savefig(backgroundPath, dpi=300)
    plt.clf()

if __name__ == "__main__":
    y = returnWeatherDataDict(locationString="Boston USA", plotGoogleMapPath='googleMap.html')
    z = returnWindRose(y)
    a = returnHeatMap(y,dataType="diffuseHorizontalRadiation",dataLabel="Diffuse Horizontal Radiation",
                      colormap='plasma')
    b = returnHeatMap(y,dataType='dryBulbTemperature',dataLabel="Dry Bulb Temperature",
                      colormap='plasma')
    c = returnSunPath(y,colormap='Blues')

    dataDict = {"diffuseHorizontalRadiation": ("Diffuse Horizontal Radiation", 'inferno'),
                'dryBulbTemperature': ("Dry Bulb Temperature", 'magma'),
                'relativeHumidity': ("Relative Humidity", 'Blues'),
                'globalHorizontalRadiation': ("Global Horizontal Radiation", 'Greens'),
                'directNormalRadiation': ("Direct Normal Radiation", 'inferno'),
                'diffuseHorizontalRadiation': ("Diffuse Horizontal Radiation", 'plasma'),
                'horizontalInfraredRadiationIntensity': ("Horizontal Infrared Radiation Intensity", 'plasma'),
                'globalHorizontalIlluminance': ("Global Horizontal Illuminance", 'plasma'),
                'directNormalIlluminance': ("Direct Normal Illuminance", 'Reds'),
                'diffuseHorizontalIlluminance': ("Diffuse Horizontal Illuminance", 'plasma')}