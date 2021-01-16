import json

def extractJson(jsonFile:str,objectName:str):
    '''
    extracts a json file and stores its objects in a list
    '''
    jsonFile = open(jsonFile)
    objects = json.load(jsonFile)     #loads data into _objects_
    jsonFile.close()
    listOfObjects = [i for i in objects[objectName]]

    return listOfObjects

def returnAccessibleStations(listOfStations):
    """
    returns a list of station NAMES which are accessible
    """
    accessibleStations=[]
    for station in listOfStations: 
        if station['Accessible']==True:
            accessibleStations.append(station["Name"])
    
    return accessibleStations

def extractinput(inputFile:str):
    fileRead = open(inputFile)
    startPosList = []
    endPosList = []
    for line in fileRead.readlines():
        stations = line.split(",")
        startPosList.append(stations[0])
        endPosList.append(stations[1][:-1])
    return startPosList, endPosList