import jsonFunctions
import json
from collections import deque
import pathfinding

extracted_json = jsonFunctions.extractJson("2.json","Nodes")
sources, destination = jsonFunctions.extractinput("2.in")

previous, dist = pathfinding.Dijkstra(extracted_json,sources[0])

print (previous)

# dict1 = extracted_json[0]
# Q={}
# for v in extracted_json:
#     Q[v["Name"]] = v

# print(Q["Yonge"]["Neighbours"])

# minN = pathfinding.smallestDistInQ(Q,"Christie","Yonge")
# print(minN)
# # for source in sources[0]:
#     # print(source)
#     #TODO: Use Djikstra on source.


# # with open("UTEK 2021/2.json","r") as f:
