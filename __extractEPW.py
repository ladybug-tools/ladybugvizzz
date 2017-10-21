import os
from __locateEPW import ClimateData
from __locateEPW import locateEPW
from ladybug.epw import EPW

def extractEPWdataset(climateDataClass,fileDownloadDirectory=None):
    """

    :param climateDataClass: An instance of the class climate data.
    :type climateDataClass: ClimateData
    :return: A dictionary containing
    """
    climateData = climateDataClass
    dataSource=climateData.download(fileDownloadDirectory)
    epwFile =climateDataClass.getEpwFile(fileDownloadDirectory)
    epwObj= EPW(epwFile)

    dataDict = {}
    dataDict['dryBulbTemperature']=list(epwObj.dryBulbTemperature)
    dataDict['dewPointTemperature'] = list(epwObj.dewPointTemperature)
    dataDict['relativeHumidity'] = list(epwObj.relativeHumidity)
    dataDict['windSpeed'] = list(epwObj.windSpeed)
    dataDict['windDirection']=list(epwObj.windDirection)
    dataDict['globalHorizontalRadiation'] = list(epwObj.globalHorizontalRadiation)
    dataDict['directNormalRadiation'] = list(epwObj.directNormalRadiation)
    dataDict['diffuseHorizontalRadiation'] = list(epwObj.diffuseHorizontalRadiation)
    dataDict['horizontalInfraredRadiationIntensity'] = list(epwObj.horizontalInfraredRadiationIntensity)
    dataDict['globalHorizontalIlluminance']=list(epwObj.globalHorizontalIlluminance)
    dataDict['directNormalIlluminance'] = list(epwObj.directNormalIlluminance)
    dataDict['diffuseHorizontalIlluminance'] = list(epwObj.diffuseHorizontalIlluminance)


    return dataDict

if __name__ =="__main__":
    from __locateEPW import locateEPW
    x = locateEPW('Djakarta Indonesia')
    #isolate the first result.
    res1 = x[0]

    #Get the climate data class.
    climData = res1.climateDataClass

    #Get weather data
    weatherDataDict = extractEPWdataset(climData)

    print(weatherDataDict['windSpeed'])
