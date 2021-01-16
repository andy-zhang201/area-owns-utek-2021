import json
#from 1a import fxn

file_1b = open('UTEK 2021/1b.json')

list_paths = json.load(file_1b)["Paths"]

lst_out = []

for path in list_paths:
    num_of_accessible_stations = fxn(path["Nodes"])
    lst_out.append(tuple(path["PathName"], num_of_accessible_stations/len(path["Nodes"])))


