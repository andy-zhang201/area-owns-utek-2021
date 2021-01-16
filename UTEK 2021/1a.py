import jsonFunctions

def output1a(accessibleStations):
    f = open("1a.out", "w")
    f.write(', '.join(accessibleStations))
    f.close()

def main():
    stations = jsonFunctions.extractJson('1a.json','Nodes')
    accessibleStations = jsonFunctions.returnAccessibleStations(stations)
    output1a(accessibleStations)

main()
