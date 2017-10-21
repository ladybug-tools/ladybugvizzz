import random

def returnRandomCity(beginsWith=None,endsWith=None):
    """
    Return a random city from the list of cities in the csv file at __epwLocations/largeCities.csv
    :param beginsWith: Filter cities starting with these letters.
    :param endsWith:  Filter cities ending with these letters.
    :return:
    """
    cityList = []
    with open('__epwLocations/largeCities.csv') as cityData:
        for lines in cityData:
            if lines.strip():
                cityList.append(lines.strip())

    if isinstance(beginsWith,basestring):
        cityList = [val for val in cityList if val.lower().startswith(beginsWith.lower())]
    if isinstance(endsWith,basestring):
        cityList = [val for val in cityList if val.lower().endswith(endsWith.lower())]

    if not cityList:
        raise Exception("No cities were found with the matching criteria.")

    return random.choice(cityList)
