import json

file_1b = open('UTEK 2021/1b.json')

list_paths = json.load(file_1b)["Paths"]

lst_out = []

for path in list_paths:
    num_of_accessible_stations = rAS(path["Nodes"])
    accessible=0
    for node in num_of_accessible_stations:
        total+=1
        if node["Accessible"]:
            accessible+=1


