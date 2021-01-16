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
    Inputs:
        listOfStations: a list of station objects (dictionaries)
    
    returns:
        List of names of accessible stations
    """
    accessibleStations=[]
    for station in listOfStations: 
        if station['Accessible']==True:
            accessibleStations.append(station["Name"])
    
    return accessibleStations

def extractinput(inputFile:str):
    '''
    Reads lines of 2 inputs and 

    inputs: 
        inputFile: name of input file ("UTEK 2021\\2.in")

    Returns:
        two lists, one of starting Stations, one of ending Stations 

    '''
    fileRead = open(inputFile)
    startPosList = []
    endPosList = []
    for line in fileRead.readlines():
        stations = line.split(",")
        startPosList.append(stations[0])
        endPosList.append(stations[1][:-1])
        
    return startPosList, endPosList