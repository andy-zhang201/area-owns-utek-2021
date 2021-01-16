import math as m
import jsonFunctions
import json
from collections import deque

'''
Here is the pseudo code for dijkstra: a common shortest path algorithm
'''


# Inputs x and y coords of 2 nodes and outputs distance between them.
def distance(x1,y1,x2,y2):
    delta_x = x2-x1
    delta_y = y2-y1
    return m.sqrt(delta_x**2+delta_y**2) #test case: print(distance(0,0,3,4))

#Queue 
# def bfs(graph,start):
#     queue=q()
#     queue.push(start)
#     while queue not empty:
#         node=queue.pop()
#         # Nodes are a part of graph
#         for each neighbour of node:
#             if neighbour not visited:
#                 push the neighbour onto the queue
#                 mark neighbour not visited

#Dijkstra function
#Graph should be list, containing nodes that are dicts
#source is a string with name of starting station

def smallestDistInQ(big_dict,name:str,source:str):
    minDistance = float("inf")
    if big_dict[name] == source:
        minNode = source
    else:
        for dic in big_dict[name]["Neighbours"]:
            if dic["Distance"] <= minDistance:
                minDistance = dic["Distance"]
                minNode = dic["Name"]
            else:
                continue
    return minNode
    
def Dijkstra(Graph, source):
    #initialize
    #vertex = station in the json
    # Dist is a dictionary. Keys are names of nodes in graph, value is the distance from source node to that node in the key.
    dist={}
    previous = {}
    Q = {}
    for v in Graph:
        # if (v["Name"]=="Finch"):
        #     print(v)

        dist[v["Name"]] = float("inf")	# initial distance from source to vertex v is set to infinite
        previous[v["Name"]] = None	# Previous node in optimal path from source
        #source is a string with name of starting station
        dist[source] = 0	# Distance from source to source
        # Q is a dictionary of nodes, key is name of node.
        Q[v["Name"]] = v

    #loop through
    while len(Q)>0:	# main loop
        u = smallestDistInQ(Q,v["Name"],source)
        print (u)
        print (Q)
        nodeDict = Q.pop(u)
        
        for neighbour in nodeDict["Neighbours"]:
            newDist = dist[u] + neighbour["Distance"]
            if newDist < dist[v["Name"]]:
                dist[v["Name"]] = newDist
                previous[v["Name"]] = u

        # del(dist[u])
            
        
    return previous

        
            
    #     remove u from Q
    #     for each neighbor v of u:	# where v has not yet been removed from Q.
    #         alt := dist[u] + dist_between(u, v)
    #         if alt < dist[v]	# Relax (u,v)
    #             dist[v] := alt
    #             previous[v] := u
	# return previous[ ]

