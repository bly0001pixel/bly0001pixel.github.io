import random
import itertools

def find_keyofvalue(dict, target):
    for key, values in dict.items():
        if target in values:
            return key

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
        #Checks if node has 0 or 1 edges
        if len(edges[node]) < 2:
            #Picks random destination node
            dest = random.randint(0,size-1)
            #Appends new edge to both nodes
            edges[node].append(dest)
            edges[dest].append(node)

    #Prints Edges
    for edge in edges:
        print(f"{edge} : {edges[edge]}")

    return edges

def pathfind_forwards(edges, origin, dest):
    #Initialise list of nodes that requires visiting
    notVisited = [i for i in range(size)]
    notVisited.remove(origin)
    
    #First layer is the origin's edges
    layer = {origin:edges[origin]}

    steps = []

    #Repeats until finds destination or stops (not connected)
    for i in range(size):
        nextLayer = {}

        #Iterates through nodes in previous layer's edges
        for startNode in layer.values():
            #Iterates through nodes in the next layer's edges
            for node in startNode:
                #Check if node has not been visited
                if node in notVisited:
                    #Return layers if destination found
                    if node == dest:
                        return steps
                    else:
                        #Record node as visited
                        notVisited.remove(node)

                        #Fill out next layer's edges for current node
                        nextLayer[node] = []
                        for nextNode in edges[node]:
                            if nextNode in notVisited:
                                nextLayer[node].append(nextNode)

            #Set next layer for next step
            layer = nextLayer.copy()
            
        #Append current layer to steps
        steps.append(nextLayer)

def pathfind_backwards(steps, origin, dest):
    route = []

    #Set starting point for backwards pass
    target = dest
    #Repeats for number of steps
    for i in range(0,len(steps),1):
        #Find previous node in route in current step's dictionary
        key = find_keyofvalue(steps[-(i+1)],target)
        #Add node to start of route
        route.insert(0, key)
        #Set node to next 
        target = key

    #Add origin and destination to route
    route.insert(0, origin)
    route.append(dest)

    return route

def main(size, minConnections):
    edges = create_network(size, minConnections)

    #Initialise random origin and destination with distance > 1 
    origin = random.randint(0,size-1)
    while True:
        dest = random.randint(0,size-1)
        if dest != origin and dest not in edges[origin]:
            break

    steps = pathfind_forwards(edges, origin, dest)
    route = pathfind_backwards(steps, origin, dest)

    #Display route and steps taken
    for step in steps:
        print(step)
    print(route)

    return edges, route