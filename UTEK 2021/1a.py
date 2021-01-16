import jsonFunctions

def output1a(accessibleStations):                                           # output function to write th output to a .out file
    f = open("1a.out", "w")
    f.write(', '.join(accessibleStations))
    f.close()

def main():
    stations = jsonFunctions.extractJson('1a.json','Nodes')                 # extract the Json file (input)
    accessibleStations = jsonFunctions.returnAccessibleStations(stations)   # use the return Accessible functions to get the list of stations that are accessible
    output1a(accessibleStations)                                            # generate the output file

main()
