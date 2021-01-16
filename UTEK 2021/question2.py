import jsonFunctions
import json
from collections import deque
import pathfinding

extracted_json = jsonFunctions.extractJson("UTEK 2021/2.json","Nodes")
sources, destination = jsonFunctions.extractinput("UTEK 2021/2.in")
# print(sources[0])

pathfinding.Dijkstra(extracted_json,sources[0])

print(dict1)
print("##########################")
print(dict2)
# for source in sources[0]:
    # print(source)
    #TODO: Use Djikstra on source.


# with open("UTEK 2021/2.json","r") as f:
