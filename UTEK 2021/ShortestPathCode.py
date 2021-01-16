import json

#reading the json file 
stationsFile = open("UTEK 2021/2.json")
inputfile = open("UTEK 2021/2.in")

#parsing the json file 
stationsDictionary = json.loads(stationsFile)

def extractinput(inputFile:str,objectName:str):
    fileRead = open(inputFile)
    startPosList = []
    endPosList = []
    for line in fileRead.readlines():
        stations = line.split(",")
        startPosList.append(stations[0])
        endPosList.append(stations[1])
    return startPosList, endPosList
        



 
    


