import pygame
from pygame import Vector2 as v2
pygame.init()
from nodes import nodes_main
import math, time

FPS, WIDTH, HEIGHT = 60, 700, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")

BLACK = (0,0,0)
GREY = (200,200,200)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

FONT1 = pygame.font.SysFont("sansserif", 60, False)
FONT2 = pygame.font.SysFont("sansserif", 30, False)

#Initialises Network Variables
size = 20
minConnections = 20

#Initialise Display Variables
margin = 80
radius = 10
center = v2(WIDTH/2,HEIGHT/2)
largeRadius = (HEIGHT/2)-(margin)
interval = 360/(size)
connectionWidth = 4
routeWidth = 6
labelDist = 40

nodes = []

class Node:
    def __init__(self, pos, num, colour):
        self.pos = pos
        self.num = num
        self.colour = colour

textBoxes = []

class TextBox:
    def __init__(self, text, pos, colour, textID):
        self.text = text
        self.colour = colour
        self.textID = textID
        if self.textID == 0:
            self.blit = FONT1.render(self.text, 0, self.colour)
        elif self.textID == 1:
            self.blit = FONT2.render(self.text, 0, self.colour)
        self.pos = v2(pos.x-(self.blit.get_width()/2),pos.y-(self.blit.get_height()/2))

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

def create_node_labels():
    for i in range(size):
        #Angle and postion of label
        angle = math.radians(interval*i)
        labelX = center.x + ((largeRadius+labelDist)*math.sin(angle))
        labelY = center.y - ((largeRadius+labelDist)*math.cos(angle))
        labelPos = v2(labelX, labelY)
        label = TextBox(str(i), labelPos, WHITE, 1)
        textBoxes.append(label)

def draw_display(connectionLines, routeLines, animationIndex):
    window.fill(BLACK)

    #Draw all edges
    for connection in connectionLines:
        pygame.draw.line(window, BLUE, connection[0], connection[1], connectionWidth)

    #Draw route according to animation progress
    for i in range(min(len(routeLines),animationIndex)):
        pygame.draw.line(window, GREEN, routeLines[i][0], routeLines[i][1], routeWidth)

    #Draw nodes
    for node in nodes:
        pygame.draw.circle(window, node.colour, node.pos, radius)

    #Draw route length when animation finishes
    if animationIndex == len(routeLines)+1:
        for textBox in textBoxes:
            if textBox.textID == 0:
                window.blit(textBox.blit, textBox.pos)

    #Draw node labels
    for textBox in textBoxes:
        if textBox.textID != 0:
            window.blit(textBox.blit, textBox.pos)

def main():
    run = True
    clock = pygame.time.Clock()

    #Run nodes.py
    route, connections, origin, dest = nodes_main(size, minConnections)

    #Create nodes and lines
    create_nodes(origin, dest)
    connectionLines = create_connections(connections)
    routeLines = create_route(route)

    #Initialise Animation Variables
    animationTime = 0.8
    animationIndex = 0
    animationClock = -FPS*animationTime

    #Create route length text
    routeLengthText = TextBox(str(len(routeLines)),v2(50,50),WHITE, 0)
    textBoxes.append(routeLengthText)

    #Create node labels
    create_node_labels()

    while run:
        clock.tick(FPS)
        animationClock += 1
        if animationClock >= animationTime*FPS:
            animationIndex = min(len(routeLines)+1,animationIndex+1)
            animationClock = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        #Draw and update frame
        draw_display(connectionLines, routeLines, animationIndex)
        pygame.display.flip()

        print(animationIndex)

    pygame.quit()

if __name__ == "__main__":
    main()