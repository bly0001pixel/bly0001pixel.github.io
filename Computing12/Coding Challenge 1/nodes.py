import random
import itertools

#Initialises Network Variables
size = 7
minConnections = 7

def create_network(size, minConenctions):
    #Creates nodes list and emtpy edges dictionary
    nodes = [i for i in range(size)]
    edges = {}
    for i in range(size):
        edges[i] = []

    #Creates all possible connections and iterable copy
    combinations = list(itertools.combinations(nodes,2))
    combinationsIter = combinations.copy()

    #Chooses minConnections number of connections
    for i in range(minConnections):
        #Chooses random remaining connection
        edge = combinationsIter[random.randint(0,len(combinationsIter)-1)]
        #Removes connection from possible connections
        combinationsIter.remove(edge)
        #Appends edge to both node's edges
        edges[edge[0]].append(edge[1])
        edges[edge[1]].append(edge[0])

    for node in edges:
        #Checks if node has no edges
        if not edges[node]:
            #Picks random destination node
            dest = random.randint(0,size-1)
            #Appends new edge to both nodes
            edges[node].append(dest)
            edges[dest].append(node)

    #Prints Edges
    for edge in edges:
        print(f"{edge} : {edges[edge]}")

    return edges, nodes

edges, nodes = create_network(size, minConnections)

def pathfind(edges, origin, dest):
    notVisited = [i for i in range(size)]
    notVisited.remove(origin)
    layer = edges[origin]
    while len(notVisited) > 0:
        nextLayer = []
        for node in layer:
            for nextNode in edges[node]:
                print(nextNode)
                if nextNode in notVisited:
                    notVisited.remove(node)
                    nextLayer.append(node)
        
        print(nextLayer)

        break

origin = random.randint(0,size-1)
while True:
    dest = random.randint(0,size-1)
    if dest != origin:
        break

print(origin)
print(dest)
print()

pathfind(edges, origin, dest)