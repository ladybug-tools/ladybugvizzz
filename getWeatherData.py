"""
This module contains a function for returning a dictionary for weather data lists.

"""
from __locateEPW import locateEPW
from __extractEPW import extractEPWdataset

def returnWeatherDataDict(locationString=None,longitude=None,latitude=None,downloadDirectory=None,
                          searchRadius=50, searchMultiplier=5, recursionLimit=5,
                          numberOfResults=10,searchDataSelection=0 ):
    """
    Return a dictionary containing weather data lists of 8760 each based on search parameters. The search parameters
    can be a generic address specified through locationString or longitude and latitude values. Either of those options
    are to be specified for this function to run.

    If both are provided longitude,latitude will be prioritized over locationString.


    At present the following outputs are supported: dryBulbTemperature, dewPointTemperature, relativeHumidity, windSpeed,
    windDirection, globalHorizontalRadiation,directNormalRadiation,diffuseHorizontalRadiation,
    horizontalInfraredRadiationIntensity,globalHorizontalIlluminance,directNormalIlluminance, diffuseHorizontalIlluminance

    Sample usage:
        #Search based on longitude latitude.

        y= returnWeatherDataDict(latitude=32.77,longitude=-96.79)

        print(y['windSpeed'])


        #Search based on location string.

        y=returnWeatherDataDict(locationString='North Pole')

        print(y['windSpeed'])

    :param locationString: A string to search weather data locations. Can be something like "Boston MA USA", or
        "North Pole"
    :param longitude: In degrees. The convention is positive for east of GMT and negative for west of GMT.
    :param latitude: In degrees. The convention is positive for north of equator and negative for south.
    :param downloadDirectory: A temporary directory for downloading weather data files. Not automatically deleted. This
        input is optional.
    :param searchRadius: Minimum search radius for locating weather data. Starts at 50 and then is increased by factors
        of searchMultiplier input.
    :param searchMultiplier: A search multiplier for setting radius.
    :param recursionLimit: Stop searching for weather data after these many recursions.
    :param numberOfResults: Number of results to store.
    :param searchDataSelection: Select this option from the number of results returned after weather data search. Defaults
        to an index of 0, which means that the first search option will be selected.
    :return:
    """
    assert locationString or ((longitude is not None) and (latitude is not None)),\
        'Either locationString (%s) or longitude(%s) and latitude(%s) should be provided'%(locationString,longitude,
                                                                                           latitude)

    if (longitude is not None) and (latitude is not None):
        x = locateEPW(longitude=longitude,latitude=latitude,searchRadius=searchRadius,searchMultiplier=searchMultiplier,
                      recursionLimit=recursionLimit,numberOfResults=numberOfResults)
    else:
        x = locateEPW(addressString=locationString,searchRadius=searchRadius,searchMultiplier=searchMultiplier,
                      recursionLimit=recursionLimit,numberOfResults=numberOfResults)
    # isolate the first result.
    res1 = x[searchDataSelection]
    # Get the climate data class.
    climData = res1.climateDataClass

    # Get weather data
    weatherDataDict = extractEPWdataset(climData,fileDownloadDirectory=downloadDirectory)

    return weatherDataDict
if __name__ == "__main__":

    y= returnWeatherDataDict(latitude=32.77,longitude=-96.79)
    print(y['windSpeed'])

    y=returnWeatherDataDict(locationString='North Pole')
    print(y['windSpeed'])