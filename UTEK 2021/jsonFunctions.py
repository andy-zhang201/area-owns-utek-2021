import json

def extractJson(jsonFile:str,objectName:str):
    '''
    extracts a json file and stores its objects in a list

    Returns the list of objects
    '''
    jsonFile = open(jsonFile)
    objects = json.load(jsonFile)     #loads data into _objects_
    jsonFile.close()
    listOfObjects = [i for i in objects[objectName]]

    return listOfObjects

def returnAccessibleStations(listOfStations):
    """
    Returns a list of station NAMES which are accessible
    """
    accessibleStations=[]
    for station in listOfStations: 
        if station['Accessible']==True:
            accessibleStations.append(station["Name"])
    
    return accessibleStations