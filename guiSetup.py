# coding=utf-8
from __future__ import print_function

import sys
from PyQt4 import QtGui
from PyQt4.QtCore import QUrl
from gui.gui import Ui_MainWindow
from __locateEPW import locateEPW,locateByAddress
from getWeatherData import returnWeatherDataDict
from getWeatherPlots import returnSunPath,returnHeatMap,returnWindRose
from utilities.colors import colorList
class Base(QtGui.QMainWindow,Ui_MainWindow):
    """
    This class sets up the UI from the imported pyuic file.
    It also instantiates the json object that will be avilable for all the tabs.
    """
    def __init__(self,parent=None):
        super(Base,self).__init__(parent)
        self.setupUi(self)
        self.defaultWindowTitle = str(self.windowTitle())
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
        self.dataDict=dict
        self.epwLocations = None
        self.currentIndex=None
        self.btnSearch.clicked.connect(self.searchChanged)
        self.listEPWlocations.clicked.connect(self.epwSelected)
        self.btnGeneratePlots.clicked.connect(self.visualize)

        self.cmbPlotType.addItems(list(dataDict.keys()))
        self.cmbColorScheme.addItems(list(colorList))
        self.weatherDataDict = None
        self.cmbPlotType.currentIndexChanged.connect(self.createHeatMap)
        self.cmbColorScheme.currentIndexChanged.connect(self.createHeatMap)
    def searchChanged(self):
        searchText = str(self.linEditSearch.text())
        if searchText:
            address,longitude,latitude = locateByAddress(searchText)
            addressString = "Address: %s\n\nLongitude: %2.3f\nLatitude: %2.3f"%(address,longitude,latitude)

            self.textEdit.setText(addressString)
        longitude,latitude= None,None
        if self.linEditLongitude.text():
            try:
                longitude = float(self.linEditLongitude.text())
            except ValueError:
                longitude = None
        if self.linEditLatitude.text():
            try:
                latitude = float(self.linEditLatitude.text())
            except ValueError:
                latitude = None

        self.listEPWlocations.clear()
        self.epwLocations = locateEPW(addressString=searchText,longitude=longitude,latitude=latitude)
        epwList = []
        for val in self.epwLocations:
            epwList.append("%s(%s), Src:%s, %s"%(val.locationName,val.distance,val.dataSource,val.country))
        self.listEPWlocations.addItems(epwList)

    def epwSelected(self):
        currentIndex = self.listEPWlocations.currentRow()
        self.currentIndex = currentIndex


    def visualize(self):
        currentWeatherData = self.epwLocations[self.currentIndex]
        climateData = currentWeatherData.climateDataClass
        longitude,latitude = climateData.longitude,climateData.latitude

        weatherDataDict = returnWeatherDataDict(longitude=longitude,latitude=latitude,
                                                plotGoogleMapPath='googlemap.html')

        self.weatherDataDict = weatherDataDict
        self.createHeatMap()
        self.webView.setUrl(QUrl('googlemap.html'))

        z = returnWindRose(weatherDataDict=weatherDataDict,filepath='windrose.png')
        x = QtGui.QPixmap('windrose.png')
        self.lblWindrose.setPixmap(x)
        self.lblWindrose.setScaledContents(True)

        z = returnSunPath(weatherDataDict=weatherDataDict,filepath='sunpath.png')
        x = QtGui.QPixmap('sunpath.png')
        self.labelSunpath.setPixmap(x)
        self.labelSunpath.setScaledContents(True)

        self.createHeatMap()

    def createHeatMap(self):

        try:
            currentColorScheme = str(self.cmbColorScheme.currentText())
            currentChart = str(self.cmbPlotType.currentText())
        except:
            currentChart= 'diffuseHorizontalRadiation'
            currentColorScheme = 'plasma'

        z = returnHeatMap(weatherDataDict=self.weatherDataDict,colormap=currentColorScheme,dataType=currentChart,
                          dataLabel='')

        a = QtGui.QPixmap(z)
        self.lblCharts.setPixmap(a)
        self.lblCharts.setScaledContents(True)



def main():
    app = QtGui.QApplication(sys.argv)

    # if len(sys.argv)>=3:
    #     jsonFile= sys.argv[-2]
    #     spaceId = int(sys.argv[-1])
    # else:
    #     jsonFile=spaceId=None

    form = Base()
    form.show()
    app.exec_()

if __name__ == "__main__":
    # sys.argv.extend([r"C:\example1\Mistrick_Stadic_Example.json", 0])

    main()