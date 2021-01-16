
import json

file_1b = open('UTEK 2021/1b.json')

list_paths = json.load(file_1b)["Paths"]

lst_out = []

for path in list_paths:
    accessible=0
    for node in path["Nodes"]:
        if node["Accessible"]:
            accessible+=1

    lst_out.append(tuple((path["PathName"], accessible/(len(path["Nodes"])-accessible))))

print(lst_out)



