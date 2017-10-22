from __locateEPW import locateEPW
from ladybug.epw import EPW
x = locateEPW('Djakarta Indonesia')
# isolate the first result.
res1 = x[0]

# Get the climate data class.
weatherData = res1.climateDataClass
weatherArchive = weatherData.download()
epw = weatherData.getEpwFile()
epwObj = EPW(epw)
longitude,latitude,meridian = epwObj.location.longitude,epwObj.location.latitude,epwObj.location.timezone
print(longitude,latitude,meridian)

