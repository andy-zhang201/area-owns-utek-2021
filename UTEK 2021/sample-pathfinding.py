'''
Here is the pseudo code for dijkstra: a common shortest path algorithm
'''

def bfs(graph,start):
    queue=q()
    queue.push(start)
    while queue not empty:
        node=queue.pop()
        for each neighbour of node:
            if neighbour not visited:
                push the neighbour onto the queue
                mark neighbour not visited


def Dijkstra(Graph, source):
    #initialize
	for each vertex v in Graph:	
        dist[v] := infinity	# initial distance from source to vertex v is set to infinite
        previous[v] := undefined	# Previous node in optimal path from source
        dist[source] := 0	# Distance from source to source
    	Q := the set of all nodes in Graph	# all nodes in the graph are unoptimized - thus are in Q
	
    #loop through
    while Q is not empty:	# main loop
        u := node in Q with smallest dist[ ]
        remove u from Q
        for each neighbor v of u:	# where v has not yet been removed from Q.
            alt := dist[u] + dist_between(u, v)
            if alt < dist[v]	# Relax (u,v)
                dist[v] := alt
                previous[v] := u
	return previous[ ]