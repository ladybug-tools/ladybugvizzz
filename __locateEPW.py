# coding=utf-8
"""
    id,
    country,
    station_name,
    data_source,
    lat,
    lon,
    http_link,
    host,
    strong_cold_stress,
    moderate_cold_stress,
    slight_cold_stress,
    no_thermal_stress,
    slight_heat_stress,
    moderate_heat_stress,
    strong_heat_stress"""
# coding=utf-8

import logging
import csv
import urllib2,urlparse,urllib
import zipfile
import os,tempfile
import warnings
from ladybug.epw import EPW
from locationCalc.longitudeLatitude import haversine
from geopy.geocoders import Nominatim
from collections import namedtuple
from operator import itemgetter
epwData = None

logger = logging.getLogger("__main__")
logger.setLevel(logging.DEBUG)
logging.basicConfig(format='%(asctime)s -%(levelname)s m:%(module)s '
'fn:%(funcName)s msg--%(message)s')



class ClimateData(object):
    """
    This is a class for organizing weather data information for
    """
    __USstatesDict = {'AK': 'Alaska','AL': 'Alabama', 'AR': 'Arkansas','AS': 'American Samoa','AZ': 'Arizona',
                      'CA': 'California','CO': 'Colorado', 'CT': 'Connecticut', 'DC': 'District of Columbia',
                      'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'GU': 'Guam', 'HI': 'Hawaii', 'IA': 'Iowa',
                      'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky','LA': 'Louisiana',
                      'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine','MI': 'Michigan','MN': 'Minnesota',
                      'MO': 'Missouri', 'MP': 'Northern Mariana Islands', 'MS': 'Mississippi', 'MT': 'Montana',
                      'NA': 'National', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire',
                      'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio', 'OK': 'Oklahoma',
                      'OR': 'Oregon', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 'RI': 'Rhode Island', 'SC': 'South Carolina',
                      'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia', 'VI': 'Virgin Islands',
                      'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'WY': 'Wyoming'}


    def __init__(self,*data):
        self.id=data[0]
        self.country=data[1]
        self.location=data[2]
        self.dataSource=data[3]
        self.latitude=float(data[4])
        self.longitude=float(data[5])
        self.host = data[7]
        self.httpLink=data[6]
        self.strongColdStress=data[8]
        self.moderateColdStress=data[9]
        self.noThermalStress=data[10]
        self.slightHeatStress=data[11]
        self.moderateHeatStress=data[12]
        self.strongHeatStress=data[13]
        self.__zipDownloaded=False

    @property
    def httpLink(self):
        return self._httpLink

    @httpLink.setter
    def httpLink(self,value):
        if self.host =='onebuilding':
            if value.startswith("http"):
                self._httpLink = value
            else:
                self._httpLink=urlparse.urljoin(r'http://climate.onebuilding.org',value)
        elif self.host=='doe':
            if value.startswith("http"):
                self._httpLink = value
            else:
                self._httpLink = urlparse.urljoin(r'https://energyplus.net/weather-download/',value[1:])

    def __str__(self):
        outputStr = ["ID: %s"%self.id]
        outputStr.append("Country: %s"%self.country)
        outputStr.append("Latitude: %s"%(self.latitude))
        outputStr.append("Longitude: %s" % (self.longitude))
        outputStr.append("DataSource: %s"%self.dataSource)
        return "\n".join(outputStr)

    @property
    def getUSstate(self):
        assert self.country == 'USA','The property "getUSstate" is only valid for USA. The country for this dataset is' \
                                     ' %s'%self.country
        location = self.location.split()[-1]
        if location in self.__USstatesDict:
            return location
        else:
            return None

    @property
    def getUSstateFullName(self):
        return self.__USstatesDict[self.getUSstate]

    def download(self,downloadPath=None,hackDownloadMode=True):
        if not downloadPath:
            downloadPath = tempfile.mkdtemp(prefix='weather')
        else:
            assert os.path.isdir(downloadPath),'The path %s must be a directory.'%downloadPath

        sourceFile = self.httpLink
        try:

            saveName = os.path.split(sourceFile)[-1]

            if downloadPath and os.path.exists(downloadPath):
                saveName = os.path.join(downloadPath,saveName)

            if os.path.exists(saveName):
                return saveName

            #Check if the file exists.
            urllib2.urlopen(sourceFile)

            urllib.urlretrieve(sourceFile,saveName)

        except urllib2.HTTPError, e:

            #There are some issues with the EnergyPlus website, where by it won't recognize certain zip file addresses.
            #However, the corresponding data files are still in the right place.
            #So, I am downloading these files separately and then making them a zip file. It is duplicating the process
            # and wasteful, but it won't break other scripts!

            if self.host == 'doe' and hackDownloadMode:
                mainLink,allStr = os.path.split(self.httpLink)
                nameOnly = os.path.split(mainLink)[-1]
                saveName = os.path.join(downloadPath,nameOnly+'.zip')

                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                            'Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}

                request_ = urllib2.Request(self.httpLink, None, headers)  # The assembled request
                response = urllib2.urlopen(request_)  # store the response

                with open(saveName,'wb') as newZipFile:
                    newZipFile.write(response.read())
            else:
                raise Exception("The file %s was not found. The following error code was returned: %s."
                            "Try a different dataset other than %s"%(sourceFile,e.code,self.host))

        except urllib2.URLError, e:
            raise Exception(e.args)

        return saveName

    def __getDataFile(self,fileType,downloadPath=None,):
        zipFileLocation = self.download(downloadPath)
        zipFileDirectory = os.path.split(zipFileLocation)[0]
        zipName = os.path.split(self.httpLink)[1]
        try:
            zipData = zipfile.ZipFile(zipFileLocation)
        #In case the existing file is corrupt, try again by removing the old file.
        except zipfile.BadZipfile:
            os.remove(self.download(downloadPath=downloadPath))
            zipData = zipfile.ZipFile(zipFileLocation)
        dataFile = [fileName for fileName in zipData.namelist() if fileName.lower().endswith(fileType)]
        assert dataFile,'The weather data archive for %s|%s does not contain any %s files.'%(self.location,self.country,fileType)

        if len(dataFile)>1:
            warnings.warn('The weather data archive for %s|%s does contains multiple %s files:\n\t%s.'
                          'Only the first file will be extracted.'%(self.location,self.country,fileType,"\n\t".join(dataFile)))

        zipData.extract(member=dataFile[0],path=zipFileDirectory)
        zipData.close()

        return os.path.join(zipFileDirectory, dataFile[0])

    def getEpwFile(self,downloadPath=None):
        return self.__getDataFile('epw',downloadPath=downloadPath)

    def getDdyFile(self,downloadPath=None):
        return self.__getDataFile('ddy',downloadPath=downloadPath)

    def getRainFile(self,downloadPath=None):
        return self.__getDataFile('rain',downloadPath=downloadPath)

    def getStatFile(self,downloadPath=None):
        return self.__getDataFile('stat',downloadPath=downloadPath)

    def getWeaFile(self,downloadPath=None):
        return self.__getDataFile('wea',downloadPath=downloadPath)

    def getClmFile(self,downloadPath=None):
        return self.__getDataFile('clm',downloadPath=downloadPath)



locationValueTuple= namedtuple('locationValue',['locationName','dataSource','country','climateDataClass','distance'])

def locateEPW(addressString=None,longitude=None,latitude=None,searchRadius=50,searchMultiplier=5,recursionLimit=5,
              numberOfResults=10):
    """
    Return a nested tuple of available epw files based on location data. Either addressString or longitude and latitude
    should be provided for a search to be relevant. The results will be returned according to proximity from the
    provided location. This proximity will be calculated based on the haversine formula.


    :param addressString: This should be a string to search for address.
    :param longitude:
    :param latitude:
    :param searchRadius: A float that specifies the initial search radius for epw files.
    :param numberOfResults: An int that tells the function to stop iterating once that many results have been located.
    :param searchMultiplier: If the desired number of results, specified by numberOfResults, have not been obtained, then
        increase the search radius by multiplying with this number.
    :param recursionLimit: Stop increasing search radius after these many recursions.
    :return:
    """


    #Read country codes as per ISO3166
    with open('__epwLocations/countryCodes.csv') as countryCodes:
        countryCd = list(csv.reader(countryCodes))[1:]
        names,alpha3,codes = zip(*countryCd)
        countryDict = dict(zip(alpha3,names))


    if addressString:
        geolocator = Nominatim()
        location = geolocator.geocode(addressString,timeout=10)
        try:
            latitude,longitude=location.latitude,location.longitude
            latStr = 'N' if location.latitude>0 else 'S'
            longStr = 'E' if location.longitude>0 else 'W'
            logger.debug("Location identified as %s at %s %s, %s %s"%(location.address,location.latitude,
                                                                      latStr,location.longitude,longStr))
        except AttributeError:
            raise Exception("No geographical locations were identified for %s. A more specific search"
                            " with zipcodes and similar identifying information will be more helpful."%addressString)
    else:
        assert longitude and latitude,'Either the addressString(%s) or longitude(%s) and latitude(%s) should be ' \
                                      'provided'%(addressString,longitude,latitude)

    weatherDatalist = []
    numberOfRecursions=1
    collectedIds=[]
    while len(weatherDatalist)<numberOfResults and numberOfRecursions<recursionLimit:
        for weatherList in ('doe.csv','epw.csv','onebuilding.csv'):
            with open('__epwLocations/%s'%weatherList) as epwValues:
                epwData = list(csv.reader(epwValues))

            ids = zip(*epwData)[1]
            for index,idVal in enumerate(ids):
                if idVal:
                    climateData = ClimateData(*epwData[index])

                    haversineDistance = haversine(longitude,latitude,climateData.longitude,climateData.latitude)
                    if (haversineDistance < searchRadius) and not(climateData.id in collectedIds):
                        weatherDatalist.append(locationValueTuple(climateData.location,climateData.dataSource,countryDict[climateData.country],
                                                                  climateData,round(haversineDistance,1)))
                        collectedIds.append(climateData.id)
                        # print(climateData.location,climateData.dataSource,climateData.country,haversineDistance)
                        #
                        # x = climateData.download(r'D:\epwDownload')
                        # epwFilePath = climateData.getEpwFile(r'D:\epwDownload')
                        # epwCls = EPW(epwPath=epwFilePath)
                        # print(list(epwCls.diffuseHorizontalRadiation))
        if len(weatherDatalist)<numberOfResults:
            numberOfRecursions+=1
            logger.debug("Search radius increased from %s to %s. Recursion count: %s of max %s. %s entries so far."%
                         (searchRadius,searchRadius*searchMultiplier,numberOfRecursions,recursionLimit,len(weatherDatalist)))
            searchRadius*=searchMultiplier

    weatherDatalist = sorted(weatherDatalist,key=itemgetter(-1))

    return weatherDatalist[:numberOfResults]



