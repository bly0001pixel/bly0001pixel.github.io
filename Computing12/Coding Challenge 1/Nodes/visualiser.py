import pygame
from pygame import Vector2 as v2
pygame.init()
from nodes import nodes_main
import math

FPS, WIDTH, HEIGHT = 60, 700, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")

BLACK = (0,0,0)
GREY = (200,200,200)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

#Initialises Network Variables
size = 15
minConnections = 10

#Initialise Display Variables
margin = 50
radius = 15
center = v2(WIDTH/2,HEIGHT/2)
largeRadius = (HEIGHT/2)-(margin)
interval = 360/(size)
connectionWidth = 3
routeWidth = 5

nodes = []

class Node:
    def __init__(self, pos, num, colour):
        self.pos = pos
        self.num = num
        self.colour = colour

def create_nodes(origin, dest):
    #Create nodes on positive x side
    for i in range(size):
        #Angle and postion of node
        angle = math.radians(interval*i)
        nodeX = center.x + (largeRadius*math.sin(angle))
        nodeY = center.y - (largeRadius*math.cos(angle))
        nodePos = v2(nodeX, nodeY)
        #Colour of node
        if i == origin:
            colour = GREEN
        elif i == dest:
            colour = RED
        else:
            colour = GREY
        #Create node object and add to list of nodes
        node = Node(nodePos, i, colour)
        nodes.append(node)

def create_connections(connections):
    connectionLines = []

    #Create list of lines for all edges
    for edge in connections:
        connectionLine = [nodes[edge[0]].pos,nodes[edge[1]].pos]
        connectionLines.append(connectionLine)

    return connectionLines

def create_route(route):
    routeLines = []

    #Create list of lines for route
    for i in range(len(route)-1):
        routeLine = [nodes[route[i]].pos,nodes[route[i+1]].pos]
        routeLines.append(routeLine)

    return routeLines

def draw_display(connectionLines, routeLines):
    window.fill(BLACK)

    #Draw all edges
    for connection in connectionLines:
        pygame.draw.line(window, BLUE, connection[0], connection[1], connectionWidth)

    #Draw route
    for routeLine in routeLines:
        pygame.draw.line(window, GREEN, routeLine[0], routeLine[1], routeWidth)

    #Draw nodes
    for node in nodes:
        pygame.draw.circle(window, node.colour, node.pos, radius)

def main():
    run = True
    clock = pygame.time.Clock()

    #Run nodes.py
    route, connections, origin, dest = nodes_main(size, minConnections)

    #Create nodes and lines
    create_nodes(origin, dest)
    connectionLines = create_connections(connections)
    routeLines = create_route(route)

    print(len(routeLines))

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        #Draw and update frame
        draw_display(connectionLines, routeLines)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()